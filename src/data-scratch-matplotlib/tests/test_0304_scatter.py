import matplotlib.pyplot as plt

from data_plots_from_scratch.c03_visualizing_data.e0304_scatter import (
    make_chart_scatter_plot,
    make_chart_scatterplot_equal_axes,
    make_chart_scatterplot_unequal_axes
)


def test_make_chart_scatter_plot():
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

    fig, ax = make_chart_scatter_plot(friends, minutes, labels)

    # Test that the correct number of points were plotted
    assert len(ax.collections[0].get_offsets()) == len(friends), "Number of points should match the number of friends."

    # Test that labels are correctly annotated
    annotations = [ann.get_text() for ann in ax.texts]
    assert annotations == labels, "Annotations should match the provided labels."

    # Test that title, xlabel, and ylabel are correctly set
    assert ax.get_title() == "Daily Minutes vs. Number of Friends", "Title should be set correctly."
    assert ax.get_xlabel() == "# of friends", "X-axis label should be set correctly."
    assert ax.get_ylabel() == "daily minutes spent on the site", "Y-axis label should be set correctly."
    plt.close('all')


def test_make_chart_scatterplot_equal_axes():
    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]

    fig, ax = make_chart_scatterplot_equal_axes(test_1_grades, test_2_grades)

    # Test that the correct number of points were plotted
    assert len(ax.collections[0].get_offsets()) == len(test_1_grades), "Number of points should match the grades."

    # Test that title, xlabel, and ylabel are correctly set
    assert ax.get_title() == "Axes Are Comparable", "Title should be set correctly."
    assert ax.get_xlabel() == "test 1 grade", "X-axis label should be set correctly."
    assert ax.get_ylabel() == "test 2 grade", "Y-axis label should be set correctly."

    # Test that the axes are equal
    assert ax.get_aspect() == 1.0, "Axes should be equal."
    plt.close('all')


def test_make_chart_scatterplot_unequal_axes():
    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]

    fig, ax = make_chart_scatterplot_unequal_axes(test_1_grades, test_2_grades)

    # Test that the correct number of points were plotted
    assert len(ax.collections[0].get_offsets()) == len(test_1_grades), "Number of points should match the grades."

    # Test that title, xlabel, and ylabel are correctly set
    assert ax.get_title() == "Axes Aren't Comparable", "Title should be set correctly."
    assert ax.get_xlabel() == "test 1 grade", "X-axis label should be set correctly."
    assert ax.get_ylabel() == "test 2 grade", "Y-axis label should be set correctly."

    # Test that the axes are not equal
    assert ax.get_aspect() != 'equal', "Axes should not be equal in this plot."
    plt.close('all')
