import matplotlib.pyplot as plt


def make_chart_pie_chart():
    plt.pie([0.95, 0.05], labels=["Uses pie charts", "Knows better"])
    # make sure pie is a circle and not an oval
    plt.axis("equal")


if __name__ == "__main__":
    make_chart_pie_chart()
    plt.savefig("pie_chart.png")
