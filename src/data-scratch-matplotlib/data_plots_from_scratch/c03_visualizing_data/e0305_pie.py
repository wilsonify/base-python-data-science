import matplotlib.pyplot as plt

from data_plots_from_scratch import initialize_plot


def make_chart_pie_chart():
    fig, ax = initialize_plot()
    ax.pie([0.95, 0.05], labels=["Uses pie charts", "Knows better"])
    # make sure pie is a circle and not an oval
    ax.axis("equal")
    return fig, ax


if __name__ == "__main__":
    make_chart_pie_chart()
    plt.savefig("pie_chart.png")
