from collections import Counter

import matplotlib.pyplot as plt

from data_plots_from_scratch import initialize_plot


def decile(grade):
    return grade // 10 * 10


def make_chart_simple_bar_chart(x, y):
    """    # bars are by default width 0.8,
    # so we'll add 0.1 to the left coordinates
    # so that each bar is centered
    # plot bars with left x-coordinates [xs], heights [num_oscars]
    # label x-axis with movie names at bar centers
    """
    fig, ax = initialize_plot()
    xs = [i + 0.1 for i, _ in enumerate(x)]
    ax.bar(xs, y)
    ax.set_title("My Favorite Movies")
    ax.set_ylabel("# of Academy Awards")
    ax.set_xticks([i + 0.5 for i, _ in enumerate(x)], x)
    return fig, ax


def make_chart_histogram(xs):
    fig, ax = initialize_plot()
    histogram = Counter(decile(x) for x in xs)
    xs = list(histogram.keys())
    ys = list(histogram.values())  # give each bar its correct height
    width = 8  # give each bar a width of 8
    ax.bar(xs, ys, width, align='edge')
    ax.set_xlim((-5, 105))  # x-axis from -5 to 105,
    ax.set_ylim((0, 5))  # y-axis from 0 to 5
    ax.set_xticks([10 * i for i in range(11)])  # x-axis labels at 0, 10, ..., 100
    ax.set_xlabel("Decile")
    ax.set_ylabel("# of Students")
    ax.set_title("Distribution of Exam 1 Grades")
    return fig, ax

def make_chart_misleading_y_axis(mentions, years):
    fig, ax = initialize_plot()
    ax.bar(years, mentions, 0.8)
    ax.set_xticks(years)
    ax.set_ylabel("# of times I heard someone say 'data science'")
    # if you don't do this, matplotlib will label the x-axis 0, 1
    # and then add a +2.013e3 off in the corner (bad matplotlib!)
    ax.ticklabel_format(useOffset=False)
    ax.set_xlim([2012.5, 2014.5])
    ax.set_ylim([499, 506])
    ax.set_title("Look at the 'Huge' Increase!")
    return fig, ax

def make_chart_corrected_y_axis(mentions, years):
    fig, ax = initialize_plot()
    ax.bar(years, mentions, 0.8)
    ax.set_xticks(years)
    ax.set_ylabel("# of times I heard someone say 'data science'")
    # if you don't do this, matplotlib will label the x-axis 0, 1
    # and then add a +2.013e3 off in the corner (bad matplotlib!)
    ax.ticklabel_format(useOffset=False)
    ax.set_xlim([2012.5, 2014.5])
    ax.set_ylim([0, 550])
    ax.set_title("Not So Huge Anymore.")
    return fig, ax

if __name__ == "__main__":
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    make_chart_simple_bar_chart(x=movies, y=num_oscars)
    plt.savefig("e030201_chart_simple_bar_chart.png")

    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    make_chart_histogram(xs=grades)
    plt.savefig("e030202_chart_histogram.png")

    mentions = [500, 505]
    years = [2013, 2014]
    make_chart_misleading_y_axis(mentions, years)
    plt.savefig("e030203_misleading_y_axis.png")

    mentions = [500, 505]
    years = [2013, 2014]
    make_chart_corrected_y_axis(mentions, years)
    plt.savefig("e030204_corrected_y_axis.png")
