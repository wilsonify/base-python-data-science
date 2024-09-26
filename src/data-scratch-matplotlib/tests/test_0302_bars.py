from collections import Counter

import matplotlib.pyplot as plt

from data_plots_from_scratch.c03_visualizing_data.e0302_bars import (
    make_chart_simple_bar_chart,
    make_chart_histogram,
    make_chart_misleading_y_axis,
    make_chart_corrected_y_axis,
    decile,
)


def test_make_chart_simple_bar_chart():
    """Test that a simple bar chart is created with the correct labels and bar heights."""
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    fig, ax = make_chart_simple_bar_chart(movies, num_oscars)

    # Test that 5 bars were created
    assert len(ax.patches) == len(movies), "Number of bars should match the number of movies."

    # Test that the heights of the bars match num_oscars
    heights = [bar.get_height() for bar in ax.patches]
    assert heights == num_oscars, "Bar heights should match the number of Oscars."

    # Test the x-axis labels
    assert ax.get_xticks().tolist() == [i + 0.5 for i in range(len(movies))], "X-ticks should be centered."
    assert [label.get_text() for label in
            ax.get_xticklabels()] == movies, "X-tick labels should match the movie titles."

    plt.close(fig)


def test_make_chart_histogram():
    """Test that the histogram chart is created with the correct bins and frequencies."""
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    fig, ax = make_chart_histogram(grades)

    histogram = Counter(decile(x) for x in grades)
    xs = list(histogram.keys())
    ys = list(histogram.values())

    # Test that the correct number of bars were created
    assert len(ax.patches) == len(xs), "Number of histogram bars should match number of deciles."

    # Test that the heights of the bars match the frequencies
    heights = [bar.get_height() for bar in ax.patches]
    assert heights == ys, "Bar heights should match the decile frequencies."

    # Test x-axis range and tick labels
    assert ax.get_xlim() == (-5, 105), "X-axis should range from -5 to 105."
    assert ax.get_xticks().tolist() == [10 * i for i in range(11)], "X-ticks should be at deciles 0, 10, ..., 100."

    plt.close(fig)


def test_make_chart_misleading_y_axis():
    """Test that the misleading y-axis chart is created with the correct axis limits."""
    mentions = [500, 505]
    years = [2013, 2014]
    fig, ax = make_chart_misleading_y_axis(mentions, years)

    # Test that 2 bars were created
    assert len(ax.patches) == len(mentions), "There should be two bars, one for each year."

    # Test the y-axis range
    assert ax.get_ylim() == (499, 506), "Y-axis should range from 499 to 506."

    plt.close(fig)


def test_make_chart_corrected_y_axis():
    """Test that the corrected y-axis chart is created with the correct axis limits."""
    mentions = [500, 505]
    years = [2013, 2014]
    fig, ax = make_chart_corrected_y_axis(mentions, years)

    # Test that 2 bars were created
    assert len(ax.patches) == len(mentions), "There should be two bars, one for each year."

    # Test the y-axis range
    assert ax.get_ylim() == (0, 550), "Y-axis should range from 0 to 550."

    plt.close(fig)
