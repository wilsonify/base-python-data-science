import math
import random
from collections import Counter

import matplotlib.image as mpimg
from matplotlib import pyplot as plt

from data_plots_from_scratch.c03_visualizing_data.e0306_state_borders import plot_state_borders
from dsl.c04_linear_algebra.e0401_vectors import (
    dot,
    scalar_multiply,
)
from dsl.c04_linear_algebra.e0402_matrices import (
    get_column,
    shape)
from dsl.c10_working_with_data.e1001_univariate import make_histogram
from dsl.c06_probability.probability import (
    binomial, )
from dsl.c06_probability.e0603_normal import random_normal, normal_pdf, normal_cdf, inverse_normal_cdf
from dsl.c08_gradient_descent.e0801_estimating_gradient import difference_quotient
from dsl.c12_k_nearest_neighbors.nearest_neighbors import cities
from dsl.c12_k_nearest_neighbors.nearest_neighbors import knn_classify
from dsl.c20_clustering.clustering import KMeans, squared_clustering_errors


def plot_normal_pdfs():
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_pdf(x, sigma=1.0) for x in xs], "-", label="mu=0,sigma=1")
    plt.plot(xs, [normal_pdf(x, sigma=2.0) for x in xs], "--", label="mu=0,sigma=2")
    plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ":", label="mu=0,sigma=0.5")
    plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], "-.", label="mu=-1,sigma=1")
    plt.legend()
    plt.show()


def recolor_image(path_to_png_file, k=5):
    img = mpimg.imread(path_to_png_file)
    pixels = [pixel for row in img for pixel in row]
    clusterer = KMeans(k)
    clusterer.train(pixels)  # this might take a while

    def recolor(pixel):
        cluster = clusterer.classify(pixel)  # index of the closest cluster
        return clusterer.means[cluster]  # mean of the closest cluster

    new_img = [[recolor(pixel) for pixel in row] for row in img]

    plt.imshow(new_img)
    plt.axis("off")
    plt.show()


def plot_squared_clustering_errors(inputs):
    ks = range(1, len(inputs) + 1)
    errors = [squared_clustering_errors(inputs, k) for k in ks]

    plt.plot(ks, errors)
    plt.xticks(ks)
    plt.xlabel("k")
    plt.ylabel("total squared error")
    plt.show()


def plot_estimated_derivative():
    def square(x):
        return x * x

    def derivative(x):
        return 2 * x

    derivative_estimate = lambda x: difference_quotient(square, x, h=0.00001)

    # plot to show they're basically the same

    x = range(-10, 10)
    plt.plot(x, map(derivative, x), "rx")  # red  x
    plt.plot(x, map(derivative_estimate, x), "b+")  # blue +
    plt.show()


def make_chart_salaries_by_tenure():
    salaries_and_tenures = [
        (83000, 8.7),
        (88000, 8.1),
        (48000, 0.7),
        (76000, 6),
        (69000, 6.5),
        (76000, 7.5),
        (60000, 2.5),
        (83000, 10),
        (48000, 1.9),
        (63000, 4.2),
    ]
    tenures = [tenure for salary, tenure in salaries_and_tenures]
    salaries = [salary for salary, tenure in salaries_and_tenures]
    plt.scatter(tenures, salaries)
    plt.xlabel("Years Experience")
    plt.ylabel("Salary")
    plt.show()


def make_graph_dot_product_as_vector_projection():
    v = [2, 1]
    w = [math.sqrt(0.25), math.sqrt(0.75)]
    c = dot(v, w)
    vonw = scalar_multiply(c, w)
    o = [0, 0]

    plt.arrow(0, 0, v[0], v[1], width=0.002, head_width=0.1, length_includes_head=True)
    plt.annotate("v", v, xytext=[v[0] + 0.1, v[1]])
    plt.arrow(0, 0, w[0], w[1], width=0.002, head_width=0.1, length_includes_head=True)
    plt.annotate("w", w, xytext=[w[0] - 0.1, w[1]])
    plt.arrow(0, 0, vonw[0], vonw[1], length_includes_head=True)
    plt.annotate(u"(vâ¢w)w", vonw, xytext=[vonw[0] - 0.1, vonw[1] + 0.1])
    plt.arrow(
        v[0],
        v[1],
        vonw[0] - v[0],
        vonw[1] - v[1],
        linestyle="dotted",
        length_includes_head=True,
    )
    plt.scatter(*zip(v, w, o), marker=".")
    plt.axis("equal")
    plt.show()


def classify_and_plot_grid(k=1):
    plots = {"Java": ([], []), "Python": ([], []), "R": ([], [])}
    markers = {"Java": "o", "Python": "s", "R": "^"}
    colors = {"Java": "r", "Python": "b", "R": "g"}

    for longitude in range(-130, -60):
        for latitude in range(20, 55):
            predicted_language = knn_classify(k, cities, [longitude, latitude])
            plots[predicted_language][0].append(longitude)
            plots[predicted_language][1].append(latitude)

    # create a scatter series for each language
    for language, (x, y) in plots.items():
        plt.scatter(
            x,
            y,
            color=colors[language],
            marker=markers[language],
            label=language,
            zorder=0,
        )

    plot_state_borders(plt, color="black")  # assume we have a function that does this

    plt.legend(loc=0)  # let matplotlib choose the location
    plt.axis([-130, -60, 20, 55])  # set the axes
    plt.title(str(k) + "-Nearest Neighbor Programming Languages")
    plt.show()


def plot_cities():
    # key is language, value is pair (longitudes, latitudes)
    plots = {"Java": ([], []), "Python": ([], []), "R": ([], [])}

    # we want each language to have a different marker and color
    markers = {"Java": "o", "Python": "s", "R": "^"}
    colors = {"Java": "r", "Python": "b", "R": "g"}

    for (longitude, latitude), language in cities:
        plots[language][0].append(longitude)
        plots[language][1].append(latitude)

    # create a scatter series for each language
    for language, (x, y) in plots.items():
        plt.scatter(
            x,
            y,
            color=colors[language],
            marker=markers[language],
            label=language,
            zorder=10,
        )

    plot_state_borders(plt)  # assume we have a function that does this

    plt.legend(loc=0)  # let matplotlib choose the location
    plt.axis([-130, -60, 20, 55])  # set the axes
    plt.title("Favorite Programming Languages")
    plt.show()


def make_hist(p, n, num_points):
    data = [binomial(p, n) for _ in range(num_points)]

    # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar(
        [x - 0.4 for x in histogram.keys()],
        [v / num_points for v in histogram.values()],
        0.8,
        color="0.75",
    )

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.show()


# noinspection PyUnresolvedReferences
def patch(x, y, hatch, color):
    """return a matplotlib 'patch' object with the specified
    location, crosshatch pattern, and color"""
    return matplotlib.patches.Rectangle(
        (x - 0.5, y - 0.5), 1, 1, hatch=hatch, fill=False, color=color
    )


# noinspection PyUnresolvedReferences
def show_weights(neuron_idx):
    weights = _network[0][neuron_idx]
    abs_weights = [abs(weight) for weight in weights]

    grid = [
        abs_weights[row: (row + 5)]  # turn the weights into a 5x5 grid
        for row in range(0, 25, 5)
    ]  # [weights[0:5], ..., weights[20:25]]

    ax = plt.gca()  # to use hatching, we'll need the axis

    ax.imshow(
        grid,  # here same as plt.imshow
        cmap=matplotlib.cm.binary,  # use white-black color scale
        interpolation="none",
    )  # plot blocks as blocks

    # cross-hatch the negative weights
    for i in range(5):  # row
        for j in range(5):  # column
            if weights[5 * i + j] < 0:  # row i, column j = weights[5*i + j]
                # add black and white hatches, so visible whether dark or light
                ax.add_patch(patch(j, i, "/", "white"))
                ax.add_patch(patch(j, i, "\\", "black"))
    plt.show()


def compare_two_distributions():
    random.seed(0)

    uniform = [random.randrange(-100, 101) for _ in range(200)]
    normal = [57 * inverse_normal_cdf(random.random()) for _ in range(200)]

    plot_histogram(uniform, 10, "Uniform Histogram")
    plot_histogram(normal, 10, "Normal Histogram")


def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()


def scatter(xs, ys1, ys2):
    plt.scatter(xs, ys1, marker=".", color="black", label="ys1")
    plt.scatter(xs, ys2, marker=".", color="gray", label="ys2")
    plt.xlabel("xs")
    plt.ylabel("ys")
    plt.legend(loc=9)
    plt.show()


def make_scatterplot_matrix():
    # first, generate some random data

    num_points = 100

    def random_row():
        row = [None, None, None, None]
        row[0] = random_normal()
        row[1] = -5 * row[0] + random_normal()
        row[2] = row[0] + row[1] + 5 * random_normal()
        row[3] = 6 if row[2] > -2 else 0
        return row

    random.seed(0)
    data = [random_row() for _ in range(num_points)]

    # then plot it

    _, num_columns = shape(data)
    fig, ax = plt.subplots(num_columns, num_columns)

    for i in range(num_columns):
        for j in range(num_columns):

            # scatter column_j on the x-axis vs column_i on the y-axis
            if i != j:
                ax[i][j].scatter(get_column(data, j), get_column(data, i))

            # unless i == j, in which case show the series name
            else:
                ax[i][j].annotate(
                    "series " + str(i),
                    (0.5, 0.5),
                    xycoords="axes fraction",
                    ha="center",
                    va="center",
                )

            # then hide axis labels except left and bottom charts
            if i < num_columns - 1:
                ax[i][j].xaxis.set_visible(False)
            if j > 0:
                ax[i][j].yaxis.set_visible(False)

    # fix the bottom right and top left axis labels, which are wrong because
    # their charts only have text in them
    ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
    ax[0][0].set_ylim(ax[0][1].get_ylim())

    plt.show()


def make_chart_scatter_plot():
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

    plt.scatter(friends, minutes)

    # label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(
            label,
            xy=(friend_count, minute_count),  # put the label with its point
            xytext=(5, -5),  # but slightly offset
            textcoords="offset points",
        )

    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.show()


def plot_normal_cdfs():
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], "-", label="mu=0,sigma=1")
    plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], "--", label="mu=0,sigma=2")
    plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ":", label="mu=0,sigma=0.5")
    plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], "-.", label="mu=-1,sigma=1")
    plt.legend(loc=4)  # bottom right
    plt.show()
