import csv
import logging
from collections import defaultdict
from logging.config import dictConfig

import dateutil
from dateutil.parser import parser

from dsl.manipulation import (
    parse_rows_with,
    parse_dict,
    group_by,
    picker,
    scale,
    rescale,
    de_mean_matrix,
    principal_component_analysis,
    transform_vector,
)
from dsl.probability import random_normal
from dsl.stats import correlation
from dsl.working_with_data import day_over_day_changes, overall_change


def read_stocks_txt(path_to_stocks):
    _data = []
    parsers = {"date": dateutil.parser.parse, "closing_price": float}
    with open(path_to_stocks, "r", encoding="utf8", newline="") as f:
        reader_dict = csv.DictReader(f, delimiter="\t")
        _data = [parse_dict(row_dict, parsers) for row_dict in reader_dict]
    return _data


def read_comma_delimited_stock_prices(path_to_csv_data):
    _data = []
    parsers = [dateutil.parser.parse, None, float]
    with open(path_to_csv_data, "r", encoding="utf8", newline="") as f:
        reader_csv = csv.reader(f)
        for line in parse_rows_with(reader_csv, parsers):
            _data.append(line)
            if any(x is None for x in line):
                logging.info("%r", f"line = {line}")

    return _data


def group_by_symbol(_data, column_name="symbol"):
    logging.info("group rows by symbol")
    by_symbol = defaultdict(list)
    for row_data in _data:
        by_symbol[row_data[column_name]].append(row_data)
    return by_symbol


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


def main1(path_to_csv_data):
    logging.info("safe parsing")
    _data = read_comma_delimited_stock_prices(path_to_csv_data)


def main2(path_to_stocks):
    xs = [random_normal() for _ in range(1000)]
    ys1 = [x + random_normal() / 2 for x in xs]
    ys2 = [-x + random_normal() / 2 for x in xs]
    logging.info("%r", f"correlation(xs, ys1) {correlation(xs, ys1)}")
    logging.info("%r", f"correlation(xs, ys2) {correlation(xs, ys2)}")
    logging.info("stocks")
    _data = read_stocks_txt(path_to_stocks)
    max_aapl_price = max(row_aapl["closing_price"] for row_aapl in _data if row_aapl["symbol"] == "AAPL")
    logging.info("%r", f"max aapl price {max_aapl_price}")

    by_symbol = group_by_symbol(_data)

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

    max_all_changes = max(all_changes, key=picker("change"))
    min_all_changes = min(all_changes, key=picker("change"))
    logging.info("%r", f"max change {max_all_changes}")
    logging.info("%r", f"min change {min_all_changes}")

    overall_change_by_month = group_by(
        lambda row_r: row_r["date"].month,
        all_changes,
        overall_change
    )
    logging.info("%r", f"overall change by month {overall_change_by_month}")


def main3():
    logging.info("rescaling")

    _data = [[1, 20, 2], [1, 30, 3], [1, 40, 4]]
    scale_data = scale(_data)
    rescale_data = rescale(_data)
    logging.info("%r", f"original: {_data}")
    logging.info("%r", f"scale: {scale_data}")
    logging.info("%r", f"rescaled: {rescale_data}")


def main4():
    logging.info("PCA")
    x_matrix_demeaned = de_mean_matrix(x_matrix_list)
    components_p = principal_component_analysis(x_matrix_demeaned, 2)
    transform_demeaned = transform_vector(x_matrix_demeaned[0], components_p)
    logging.info("%r", "principal components {}".format(components_p))
    logging.info("%r", "first point {}".format(x_matrix_demeaned[0]))
    logging.info("%r", f"first point transformed {transform_demeaned}")


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main1(path_to_csv_data="/home/thom/repos/base-python-data-science/tests/data/comma_delimited_stock_prices.csv")
    main2(path_to_stocks="/home/thom/repos/base-python-data-science/tests/data/stocks.txt")
    main3()
    main4()
