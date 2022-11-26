from collections import Counter

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def make_chart_simple_line_chart():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    fig = plt.figure(figsize=(8, 5))
    gs = GridSpec(nrows=1, ncols=1, height_ratios=[1])
    ax1 = fig.add_subplot(gs[0])
    create_line_chart(ax1, gdp, years)
    fig.tight_layout()
    plt.show()


def create_line_chart(ax, x, y):
    ax.plot(x, y, color="green", marker="o", linestyle="solid")  # create a line chart, years on x-axis, gdp on y-axis
    ax.set_title("Nominal GDP")  # add a title
    ax.set_ylabel("Billions of $")  # add a label to the y-axis


def make_chart_simple_bar_chart():
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    fig = plt.figure(figsize=(8, 5))
    gs = GridSpec(nrows=1, ncols=1, height_ratios=[1])
    ax1 = fig.add_subplot(gs[0])

    simple_bar_chart(ax1, movies, num_oscars)

    plt.show()


def simple_bar_chart(ax, x, y):
    # bars are by default width 0.8,
    # so we'll add 0.1 to the left coordinates
    # so that each bar is centered
    # plot bars with left x-coordinates [xs], heights [num_oscars]
    # label x-axis with movie names at bar centers

    xs = [i + 0.1 for i, _ in enumerate(x)]
    ax.bar(xs, y)
    ax.set_title("My Favorite Movies")
    ax.set_ylabel("# of Academy Awards")
    ax.set_xticks([i + 0.5 for i, _ in enumerate(x)], x)


def make_chart_histogram():
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    fig = plt.figure(figsize=(8, 5))
    gs = GridSpec(nrows=1, ncols=1, height_ratios=[1])
    ax1 = fig.add_subplot(gs[0])
    simple_histogram(ax1, grades)
    plt.show()


def simple_histogram(ax, grades):
    def decile(grade):
        return grade // 10 * 10

    histogram = Counter(decile(grade) for grade in grades)
    xs = histogram.keys()
    ys = histogram.values()  # give each bar its correct height
    width = 8  # give each bar a width of 8
    ax.bar(xs, ys, width, align='edge')
    ax.set_xlim((-5, 105))  # x-axis from -5 to 105,
    ax.set_ylim((0, 5))  # y-axis from 0 to 5
    ax.set_xticks([10 * i for i in range(11)])  # x-axis labels at 0, 10, ..., 100
    ax.set_xlabel("Decile")
    ax.set_ylabel("# of Students")
    ax.set_title("Distribution of Exam 1 Grades")


def make_chart_misleading_y_axis(mislead=True):
    mentions = [500, 505]
    years = [2013, 2014]

    misleading_y(mentions, mislead, years)
    plt.show()


def misleading_y(ax,mentions, mislead, years):
    ax.bar([2012.6, 2013.6], mentions, 0.8)
    ax.set_xticks(years)
    ax.set_ylabel("# of times I heard someone say 'data science'")
    # if you don't do this, matplotlib will label the x-axis 0, 1
    # and then add a +2.013e3 off in the corner (bad matplotlib!)
    ax.set_xticklabel_format(useOffset=False)
    ax.set_xlim([2012.5, 2014.5])
    ax.set_ylim([499, 506])
    ax.set_title("Look at the 'Huge' Increase!")


def leading_y(mentions, mislead, years):
    plt.bar([2012.6, 2013.6], mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("# of times I heard someone say 'data science'")
    # if you don't do this, matplotlib will label the x-axis 0, 1
    # and then add a +2.013e3 off in the corner (bad matplotlib!)
    plt.ticklabel_format(useOffset=False)
    plt.axis([2012.5, 2014.5, 0, 550])
    plt.title("Not So Huge Anymore.")


def make_chart_several_line_charts():
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error = [x + y for x, y in zip(variance, bias_squared)]

    xs = range(len(variance))

    # we can make multiple calls to plt.plot
    # to show multiple series on the same chart
    plt.plot(xs, variance, "g-", label="variance")  # green solid line
    plt.plot(xs, bias_squared, "r-.", label="bias^2")  # red dot-dashed line
    plt.plot(xs, total_error, "b:", label="total error")  # blue dotted line

    # because we've assigned labels to each series
    # we can get a legend for free
    # loc=9 means "top center"
    plt.legend(loc=9)
    plt.xlabel("model complexity")
    plt.title("The Bias-Variance Tradeoff")
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


def make_chart_scatterplot_axes(equal_axes=False):
    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]

    plt.scatter(test_1_grades, test_2_grades)
    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")

    if equal_axes:
        plt.title("Axes Are Comparable")
        plt.axis("equal")
    else:
        plt.title("Axes Aren't Comparable")

    plt.show()


def make_chart_pie_chart():
    plt.pie([0.95, 0.05], labels=["Uses pie charts", "Knows better"])

    # make sure pie is a circle and not an oval
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    make_chart_simple_line_chart()

    make_chart_simple_bar_chart()

    make_chart_histogram()

    # make_chart_misleading_y_axis(mislead=True)

    # make_chart_misleading_y_axis(mislead=False)

    # make_chart_several_line_charts()

    # make_chart_scatterplot_axes(equal_axes=False)

    # make_chart_scatterplot_axes(equal_axes=True)

    # make_chart_pie_chart()
