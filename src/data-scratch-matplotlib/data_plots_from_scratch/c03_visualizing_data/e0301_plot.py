import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def initialize_plot():
    """
    drop in replacement for plt.subplots() using grid-spec
    """
    fig = plt.figure(figsize=(8, 5))
    gs = GridSpec(nrows=1, ncols=1, height_ratios=[1])
    ax = fig.add_subplot(gs[0])
    return fig, ax


def plot_with_pyplot(x, y):
    """
    Creates a simple plot using matplotlib's pyplot module.
    Returns the figure object to allow testable interactions with it.
    """
    fig, ax = initialize_plot()
    ax.plot(x, y)
    return fig, ax


if __name__ == "__main__":
    x = [1, 2, 3]
    y = [4, 5, 6]
    plot_with_pyplot(x, y)
    plt.savefig("e0301_plot_with_pyplot.png")
