import matplotlib.pyplot as plt
import pytest

from data_plots_from_scratch.c03_visualizing_data.e0305_pie import (
    make_chart_pie_chart
)


def test_make_chart_pie_chart():
    fig, ax = make_chart_pie_chart()

    # Test if a pie chart was created
    assert len(ax.patches) > 0, "Pie chart should contain patches."

    # Check that the pie chart slices add up to 100%
    pie_wedges = [p.theta2 - p.theta1 for p in ax.patches]
    assert sum(pie_wedges) == pytest.approx(360), "Pie slices should add up to 360 degrees."

    # Test if the labels are correct
    labels = [text.get_text() for text in ax.texts]
    assert labels == ["Uses pie charts", "Knows better"], "Labels should be 'Uses pie charts' and 'Knows better'."

    # Test if the aspect ratio is set to 'equal' (circle)
    assert ax.get_aspect() == 1.0, "The pie chart should be a circle (aspect ratio should be 'equal')."
    plt.close('all')
