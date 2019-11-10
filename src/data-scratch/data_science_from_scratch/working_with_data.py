import csv
import logging
import math
import os
import random
from collections import Counter, defaultdict
from functools import partial, reduce
from logging.config import dictConfig

import dateutil.parser
from data_science_from_scratch import config
from data_science_from_scratch.library.gradient_descent import (
    maximize_stochastic,
    maximize_batch,
)
from data_science_from_scratch.library.linear_algebra import (
    shape,
    get_column,
    make_matrix,
    vector_sum,
    dot,
    magnitude,
    vector_subtract,
    scalar_multiply,
)
from data_science_from_scratch.library.probability import inverse_normal_cdf
from data_science_from_scratch.library.stats import correlation, standard_deviation, mean


def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)


def random_normal():
    """returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(random.random())


def correlation_matrix(data):
    """returns the num_columns x num_columns matrix whose (i, j)th entry
    is the correlation between columns i and j of data"""

    _, num_columns = shape(data)

    def matrix_entry(i, j):
        return correlation(get_column(data, i), get_column(data, j))

    return make_matrix(num_columns, num_columns, matrix_entry)


def parse_row(input_row, parsers):
    return [
        try_or_none(parser)(value) if parser is not None else value
        for value, parser in zip(input_row, parsers)
    ]


def parse_rows_with(reader, parsers):
    """wrap a reader to apply the parsers to each of its rows"""
    for row in reader:
        yield parse_row(row, parsers)


def try_or_none(arbitrary_function):
    """wraps f to return None if f raises an exception
    assumes f takes only one input"""

    def f_or_none(x):
        try:
            return arbitrary_function(x)
        except (ValueError, IndexError, KeyError, OSError):
            return None

    return f_or_none


def try_parse_field(field_name, value, parser_dict):
    """try to parse value using the appropriate function from parser_dict"""
    parser = parser_dict.get(field_name)  # None if no such entry
    if parser is not None:
        return try_or_none(parser)(value)
    else:
        return value


def parse_dict(input_dict, parser_dict):
    return {
        field_name: try_parse_field(field_name, value, parser_dict)
        for field_name, value in input_dict.items()
    }


#
#
# MANIPULATING DATA
#
#


def picker(field_name):
    """returns a function that picks a field out of a dict"""
    return lambda row: row[field_name]


def pluck(field_name, rows):
    """turn a list of dicts into the list of field_name values"""
    return map(picker(field_name), rows)


def group_by(grouper, rows, value_transform=None):
    # key is output of grouper, value is list of rows
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)
    if value_transform is None:
        return grouped
    else:
        return {key: value_transform(rows) for key, rows in grouped.items()}


def percent_price_change(yesterday, today):
    return today["closing_price"] / yesterday["closing_price"] - 1


def day_over_day_changes(grouped_rows):
    # sort the rows by date
    ordered = sorted(grouped_rows, key=picker("date"))
    # zip with an offset to get pairs of consecutive days
    return [
        {
            "symbol": today["symbol"],
            "date": today["date"],
            "change": percent_price_change(yesterday, today),
        }
        for yesterday, today in zip(ordered, ordered[1:])
    ]


#
#
# RESCALING DATA
#
#


def scale(data_matrix):
    num_rows, num_cols = shape(data_matrix)
    means = [mean(get_column(data_matrix, j)) for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data_matrix, j)) for j in range(num_cols)]
    return means, stdevs


def rescale(data_matrix):
    """rescales the input data so that each column
    has mean 0 and standard deviation 1
    ignores columns with no deviation"""
    means, stdevs = scale(data_matrix)

    def rescaled(i, j):
        if stdevs[j] > 0:
            return (data_matrix[i][j] - means[j]) / stdevs[j]
        else:
            return data_matrix[i][j]

    num_rows, num_cols = shape(data_matrix)
    return make_matrix(num_rows, num_cols, rescaled)


#
# DIMENSIONALITY REDUCTION
#


def de_mean_matrix(a_matrix):
    """returns the result of subtracting from every value in A the mean
    value of its column. the resulting matrix has mean 0 in every column"""
    nr, nc = shape(a_matrix)
    column_means, _ = scale(a_matrix)
    return make_matrix(nr, nc, lambda i, j: a_matrix[i][j] - column_means[j])


def direction(w):
    mag = magnitude(w)
    return [w_i / mag for w_i in w]


def directional_variance_i(x_i, w):
    """the variance of the row x_i in the direction w"""
    return dot(x_i, direction(w)) ** 2


def directional_variance(x_matrix, w):
    """the variance of the data in the direction w"""
    return sum(directional_variance_i(x_i, w) for x_i in x_matrix)


def directional_variance_gradient_i(x_i, w):
    """the contribution of row x_i to the gradient of
    the direction-w variance"""
    projection_length = dot(x_i, direction(w))
    return [2 * projection_length * x_ij for x_ij in x_i]


def directional_variance_gradient(x_matrix, w):
    return vector_sum(directional_variance_gradient_i(x_i, w) for x_i in x_matrix)


def first_principal_component(x_matrix):
    guess = [1 for _ in x_matrix[0]]
    unscaled_maximizer = maximize_batch(
        partial(directional_variance, x_matrix),  # is now a function of w
        partial(directional_variance_gradient, x_matrix),  # is now a function of w
        guess,
    )
    return direction(unscaled_maximizer)


def first_principal_component_sgd(matrix_x):
    guess = [1 for _ in matrix_x[0]]
    unscaled_maximizer = maximize_stochastic(
        lambda x, _, w: directional_variance_i(x, w),
        lambda x, _, w: directional_variance_gradient_i(x, w),
        matrix_x,
        [None for _ in matrix_x],
        guess,
    )
    return direction(unscaled_maximizer)


def project(v, w):
    """return the projection of v onto w"""
    coefficient = dot(v, w)
    return scalar_multiply(coefficient, w)


def remove_projection_from_vector(v, w):
    """projects v onto w and subtracts the result from v"""
    return vector_subtract(v, project(v, w))


def remove_projection(x_matrix, w):
    """for each row of X
    projects the row onto w, and subtracts the result from the row"""
    return [remove_projection_from_vector(x_i, w) for x_i in x_matrix]


def principal_component_analysis(x_vector, num_components):
    components = []
    for _ in range(num_components):
        component = first_principal_component(x_vector)
        components.append(component)
        x_vector = remove_projection(x_vector, component)

    return components


def transform_vector(v, components):
    return [dot(v, w) for w in components]


def transform(x_vector, components):
    return [transform_vector(x_i, components) for x_i in x_vector]


def main(path_to_csv_data, path_to_stocks):
    xs = [random_normal() for _ in range(1000)]
    ys1 = [x + random_normal() / 2 for x in xs]
    ys2 = [-x + random_normal() / 2 for x in xs]

    x_matrix_list = [
        [20.9666776351559, -13.1138080189357],
        [22.7719907680008, -19.8890894944696],
        [25.6687103160153, -11.9956004517219],
        [18.0019794950564, -18.1989191165133],
        [21.3967402102156, -10.8893126308196],
        [0.443696899177716, -19.7221132386308],
        [29.9198322142127, -14.0958668502427],
        [19.0805843080126, -13.7888747608312],
        [16.4685063521314, -11.2612927034291],
        [21.4597664701884, -12.4740034586705],
        [3.87655283720532, -17.575162461771],
        [34.5713920556787, -10.705185165378],
        [13.3732115747722, -16.7270274494424],
        [20.7281704141919, -8.81165591556553],
        [24.839851437942, -12.1240962157419],
        [20.3019544741252, -12.8725060780898],
        [21.9021426929599, -17.3225432396452],
        [23.2285885715486, -12.2676568419045],
        [28.5749111681851, -13.2616470619453],
        [29.2957424128701, -14.6299928678996],
        [15.2495527798625, -18.4649714274207],
        [26.5567257400476, -9.19794350561966],
        [30.1934232346361, -12.6272709845971],
        [36.8267446011057, -7.25409849336718],
        [32.157416823084, -10.4729534347553],
        [5.85964365291694, -22.6573731626132],
        [25.7426190674693, -14.8055803854566],
        [16.237602636139, -16.5920595763719],
        [14.7408608850568, -20.0537715298403],
        [6.85907008242544, -18.3965586884781],
        [26.5918329233128, -8.92664811750842],
        [-11.2216019958228, -27.0519081982856],
        [8.93593745011035, -20.8261235122575],
        [24.4481258671796, -18.0324012215159],
        [2.82048515404903, -22.4208457598703],
        [30.8803004755948, -11.455358009593],
        [15.4586738236098, -11.1242825084309],
        [28.5332537090494, -14.7898744423126],
        [40.4830293441052, -2.41946428697183],
        [15.7563759125684, -13.5771266003795],
        [19.3635588851727, -20.6224770470434],
        [13.4212840786467, -19.0238227375766],
        [7.77570680426702, -16.6385739839089],
        [21.4865983854408, -15.290799330002],
        [12.6392705930724, -23.6433305964301],
        [12.4746151388128, -17.9720169566614],
        [23.4572410437998, -14.602080545086],
        [13.6878189833565, -18.9687408182414],
        [15.4077465943441, -14.5352487124086],
        [20.3356581548895, -10.0883159703702],
        [20.7093833689359, -12.6939091236766],
        [11.1032293684441, -14.1383848928755],
        [17.5048321498308, -9.2338593361801],
        [16.3303688220188, -15.1054735529158],
        [26.6929062710726, -13.306030567991],
        [34.4985678099711, -9.86199941278607],
        [39.1374291499406, -10.5621430853401],
        [21.9088956482146, -9.95198845621849],
        [22.2367457578087, -17.2200123442707],
        [10.0032784145577, -19.3557700653426],
        [14.045833906665, -15.871937521131],
        [15.5640911917607, -18.3396956121887],
        [24.4771926581586, -14.8715313479137],
        [26.533415556629, -14.693883922494],
        [12.8722580202544, -21.2750596021509],
        [24.4768291376862, -15.9592080959207],
        [18.2230748567433, -14.6541444069985],
        [4.1902148367447, -20.6144032528762],
        [12.4332594022086, -16.6079789231489],
        [20.5483758651873, -18.8512560786321],
        [17.8180560451358, -12.5451990696752],
        [11.0071081078049, -20.3938092335862],
        [8.30560561422449, -22.9503944138682],
        [33.9857852657284, -4.8371294974382],
        [17.4376502239652, -14.5095976075022],
        [29.0379635148943, -14.8461553663227],
        [29.1344666599319, -7.70862921632672],
        [32.9730697624544, -15.5839178785654],
        [13.4211493998212, -20.150199857584],
        [11.380538260355, -12.8619410359766],
        [28.672631499186, -8.51866271785711],
        [16.4296061111902, -23.3326051279759],
        [25.7168371582585, -13.8899296143829],
        [13.3185154732595, -17.8959160024249],
        [3.60832478605376, -25.4023343597712],
        [39.5445949652652, -11.466377647931],
        [25.1693484426101, -12.2752652925707],
        [25.2884257196471, -7.06710309184533],
        [6.77665715793125, -22.3947299635571],
        [20.1844223778907, -16.0427471125407],
        [25.5506805272535, -9.33856532270204],
        [25.1495682602477, -7.17350567090738],
        [15.6978431006492, -17.5979197162642],
        [37.42780451491, -10.843637288504],
        [22.974620174842, -10.6171162611686],
        [34.6327117468934, -9.26182440487384],
        [34.7042513789061, -6.9630753351114],
        [15.6563953929008, -17.2196961218915],
        [25.2049825789225, -14.1592086208169],
    ]

    logging.info("%r", "correlation(xs, ys1) {}".format(correlation(xs, ys1)))
    logging.info("%r", "correlation(xs, ys2) {}".format(correlation(xs, ys2)))

    # safe parsing

    _data = []

    with open(path_to_csv_data, "r", encoding="utf8", newline="") as f:
        reader_csv = csv.reader(f)
        for line in parse_rows_with(reader_csv, [dateutil.parser.parse, None, float]):
            _data.append(line)

    for row_data in _data:
        if any(x is None for x in row_data):
            logging.info("%r", "row_data = {}".format(row_data))

    logging.info("stocks")
    with open(path_to_stocks, "r", encoding="utf8", newline="") as f:
        reader_dict = csv.DictReader(f, delimiter="\t")
        _data = [
            parse_dict(
                row_dict, {"date": dateutil.parser.parse, "closing_price": float}
            )
            for row_dict in reader_dict
        ]

    max_aapl_price = max(
        row_aapl["closing_price"] for row_aapl in _data if row_aapl["symbol"] == "AAPL"
    )
    logging.info("%r", "max aapl price {}".format(max_aapl_price))

    # group rows by symbol
    by_symbol = defaultdict(list)

    for row_data in _data:
        by_symbol[row_data["symbol"]].append(row_data)

    # use a dict comprehension to find the max for each symbol
    max_price_by_symbol = {
        symbol: max(row_of_group["closing_price"] for row_of_group in grouped_rows)
        for symbol, grouped_rows in by_symbol.items()
    }
    logging.info("%r", "max price by symbol {}".format(max_price_by_symbol))

    # key is symbol, value is list of "change" dicts
    changes_by_symbol = group_by(picker("symbol"), _data, day_over_day_changes)
    # collect all "change" dicts into one big list
    all_changes = [
        change for changes in changes_by_symbol.values() for change in changes
    ]

    logging.info("%r", "max change {}".format(max(all_changes, key=picker("change"))))
    logging.info("%r", "min change {}".format(min(all_changes, key=picker("change"))))

    logging.info(
        """to combine percent changes, we add 1 to each, multiply them, and subtract 1)
    # for instance, if we combine +10% and -20%, the overall change is
    # (1 + 10%) * (1 - 20%) - 1 = 1.1 * .8 - 1 = -12%"""
    )

    def combine_pct_changes(pct_change1, pct_change2):
        return (1 + pct_change1) * (1 + pct_change2) - 1

    def overall_change(changes):
        return reduce(combine_pct_changes, pluck("change", changes))

    overall_change_by_month = group_by(
        lambda row_r: row_r["date"].month, all_changes, overall_change
    )
    logging.info("%r", "overall change by month {}".format(overall_change_by_month))

    logging.info("rescaling")

    _data = [[1, 20, 2], [1, 30, 3], [1, 40, 4]]

    logging.info("%r", "original: {}".format(_data))
    logging.info("%r", "scale: {}".format(scale(_data)))
    logging.info("%r", "rescaled: {}".format(rescale(_data)))

    logging.info("PCA")

    x_matrix_demeaned = de_mean_matrix(x_matrix_list)
    components_p = principal_component_analysis(x_matrix_demeaned, 2)
    logging.info("%r", "principal components {}".format(components_p))
    logging.info("%r", "first point {}".format(x_matrix_demeaned[0]))
    logging.info(
        "%r", "first point transformed {}".format(transform_vector(x_matrix_demeaned[0], components_p))
    )


if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)
    main(
        path_to_csv_data=os.path.join(
            config.LOCAL_DATA_DIR, "comma_delimited_stock_prices.csv"
        ), path_to_stocks=os.path.join(config.LOCAL_DATA_DIR, "stocks.txt")
    )
