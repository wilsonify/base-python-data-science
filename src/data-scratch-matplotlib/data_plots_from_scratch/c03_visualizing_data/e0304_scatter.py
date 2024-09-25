import matplotlib.pyplot as plt

from data_plots_from_scratch import initialize_plot


def make_chart_scatter_plot(friends, minutes, labels):
    fig, ax = initialize_plot()
    ax.scatter(friends, minutes)

    # label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        ax.annotate(
            label,
            xy=(friend_count, minute_count),  # put the label with its point
            xytext=(5, -5),  # but slightly offset
            textcoords="offset points",
        )

    ax.set_title("Daily Minutes vs. Number of Friends")
    ax.set_xlabel("# of friends")
    ax.set_ylabel("daily minutes spent on the site")
    return fig, ax


def make_chart_scatterplot_equal_axes(x, y):
    fig, ax = initialize_plot()
    ax.scatter(x, y)
    ax.set_xlabel("test 1 grade")
    ax.set_ylabel("test 2 grade")
    ax.set_title("Axes Are Comparable")
    ax.axis("equal")
    return fig, ax


def make_chart_scatterplot_unequal_axes(x, y):
    fig, ax = initialize_plot()
    ax.scatter(x, y)
    ax.set_xlabel("test 1 grade")
    ax.set_ylabel("test 2 grade")
    ax.set_title("Axes Aren't Comparable")
    return fig, ax


if __name__ == "__main__":
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    make_chart_scatter_plot(friends, minutes, labels)
    plt.savefig("e030401_chart_scatter_plot.png")
    plt.close()

    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]
    make_chart_scatterplot_equal_axes(test_1_grades, test_2_grades)
    plt.savefig("e030402_scatterplot_equal_axes.png")
    plt.close()

    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]
    make_chart_scatterplot_unequal_axes(test_1_grades, test_2_grades)
    plt.savefig("e030403_scatterplot_unequal_axes.png")
    plt.close()
