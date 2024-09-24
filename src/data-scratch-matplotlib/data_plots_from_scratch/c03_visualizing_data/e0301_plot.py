import matplotlib.pyplot as plt


def plot_with_pyplot(x, y):
    """
    Creates a simple plot using matplotlib's pyplot module.
    Returns the figure object to allow testable interactions with it.
    """
    fig, ax = plt.subplots()
    ax.plot(x, y)


if __name__ == "__main__":
    x = [1, 2, 3]
    y = [4, 5, 6]
    plot_with_pyplot(x, y)
    plt.savefig("e0301_plot_with_pyplot.png")
