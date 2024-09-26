from matplotlib import pyplot as plt

from data_plots_from_scratch.c03_visualizing_data.e0303_lines import (
    make_chart_simple_line_chart,
    make_chart_several_line_charts
)


def test_make_chart_simple_line_chart():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    fig, ax = make_chart_simple_line_chart(years, gdp)

    # Test if the correct number of points are plotted
    assert len(ax.lines[0].get_xydata()) == len(years), "Number of points should match the years."

    # Test line properties
    assert ax.lines[0].get_color() == "green", "Line color should be green."
    assert ax.lines[0].get_marker() == "o", "Marker should be a circle (o)."
    assert ax.lines[0].get_linestyle() == "-", "Line style should be solid."

    # Test labels and title
    assert ax.get_title() == "Nominal GDP", "Title should be 'Nominal GDP'."
    assert ax.get_ylabel() == "Billions of $", "Y-axis label should be 'Billions of $'."
    plt.close()

def test_make_chart_several_line_charts():
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

    fig, ax = make_chart_several_line_charts(variance, bias_squared)

    # Test if the correct number of points are plotted for each series
    assert len(ax.lines[0].get_xydata()) == len(variance), "Number of points for variance should match."
    assert len(ax.lines[1].get_xydata()) == len(bias_squared), "Number of points for bias_squared should match."

    # Test line colors and styles
    assert ax.lines[0].get_color() == "g", "Variance line color should be green."
    assert ax.lines[0].get_linestyle() == "-", "Variance line should be solid."
    assert ax.lines[1].get_color() == "r", "Bias^2 line color should be red."
    assert ax.lines[1].get_linestyle() == "-.", "Bias^2 line should be dot-dashed."
    assert ax.lines[2].get_color() == "b", "Total error line color should be blue."
    assert ax.lines[2].get_linestyle() == ":", "Total error line should be dotted."

    # Test legend and labels
    legend_texts = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_texts == ["variance", "bias^2", "total error"], "Legend labels should match."
    assert ax.get_xlabel() == "model complexity", "X-axis label should be 'model complexity'."
    assert ax.get_title() == "The Bias-Variance Tradeoff", "Title should be 'The Bias-Variance Tradeoff'."
    plt.close()