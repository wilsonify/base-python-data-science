import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def make_chart_simple_line_chart(x, y):
    fig = plt.figure(figsize=(8, 5))
    gs = GridSpec(nrows=1, ncols=1, height_ratios=[1])
    ax = fig.add_subplot(gs[0])
    # create a line chart, years on x-axis, gdp on y-axis
    ax.plot(x, y, color="green", marker="o", linestyle="solid")
    ax.set_title("Nominal GDP")  # add a title
    ax.set_ylabel("Billions of $")  # add a label to the y-axis
    fig.tight_layout()
    return fig, ax


def make_chart_several_line_charts(variance, bias_squared):
    fig = plt.figure(figsize=(8, 5))
    gs = GridSpec(nrows=1, ncols=1, height_ratios=[1])
    ax = fig.add_subplot(gs[0])
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = range(len(variance))
    # we can make multiple calls to plt.plot
    # to show multiple series on the same chart
    ax.plot(xs, variance, "g-", label="variance")  # green solid line
    ax.plot(xs, bias_squared, "r-.", label="bias^2")  # red dot-dashed line
    ax.plot(xs, total_error, "b:", label="total error")  # blue dotted line
    # because we've assigned labels to each series
    # we can get a legend for free
    # loc=9 means "top center"
    ax.legend(loc=9)
    ax.set_xlabel("model complexity")
    ax.set_title("The Bias-Variance Tradeoff")
    return fig, ax


if __name__ == "__main__":
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    make_chart_simple_line_chart(x=years, y=gdp)
    plt.savefig("e030301_simple_line_chart.png")

    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    make_chart_several_line_charts(variance, bias_squared)
    plt.savefig("e030302_several_line_charts.png")
