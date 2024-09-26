import matplotlib.pyplot as plt

from data_plots_from_scratch.c03_visualizing_data.e0301_plot import plot_with_pyplot


def test_plot_with_pyplot():
    """
    Tests the plot_with_pyplot function by verifying the returned
    figure and axis objects and the data plotted.
    """
    x = [1, 2, 3]
    y = [4, 5, 6]
    fig, ax = plot_with_pyplot(x, y)

    # Check if a line plot was created
    assert len(ax.lines) == 1, "There should be one line plot."

    # Check the x and y data of the plot
    line = ax.lines[0]
    assert list(line.get_xdata()) == x, "X data should match the input."
    assert list(line.get_ydata()) == y, "Y data should match the input."

    plt.close(fig)  # Close the figure after testing to free resources
