import matplotlib.pyplot as plt


def make_chart_scatter_plot(friends, minutes, labels):
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


def make_chart_scatterplot_equal_axes(x, y):
    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]
    plt.scatter(test_1_grades, test_2_grades)
    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")
    plt.title("Axes Are Comparable")
    plt.axis("equal")


def make_chart_scatterplot_unequal_axes(x, y):
    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]
    plt.scatter(test_1_grades, test_2_grades)
    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")
    plt.title("Axes Aren't Comparable")


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
