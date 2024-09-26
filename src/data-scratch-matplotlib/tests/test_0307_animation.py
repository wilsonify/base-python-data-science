from os import remove
from os.path import exists

from matplotlib import pyplot as plt

from data_plots_from_scratch.c03_visualizing_data.e0307_animation import LineTracker


def test_line_tracker_create_plot():
    """Test the create_plot method."""
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    output_file = "simple_line_chart.png"
    lt = LineTracker(title="Nominal GDP", ylabel="Billions of $")
    lt.create_plot(x=years, y=gdp, output_path=output_file)
    assert len(lt.ax0.lines) == 2, "There should be one line plotted."
    assert exists(output_file), "The plot image should be saved."
    plt.close()
    remove(output_file)


def test_line_tracker_update_plot():
    """Test the update_plot method."""
    years = [1950, 1960, 1970]
    gdp = [300.2, 543.3, 1075.9]
    lt = LineTracker(title="Nominal GDP", ylabel="Billions of $")
    lt.update_plot(x=years, y=gdp)
    assert len(lt.ax0.collections) == 1, "There should be one scatter plot created."
    assert len(lt.ax0.lines) == 2, "There should be two lines (the static and updated one)."
    plt.close()


def test_line_tracker_animate():
    """Test the animate method."""
    years = [1950, 1960, 1970]
    gdp = [300.2, 543.3, 1075.9]
    output_file = "animated_line_chart.gif"
    lt = LineTracker(title="Nominal GDP", ylabel="Billions of $")
    lt.animate(x=years, y=gdp, output_path=output_file)
    assert len(lt.artists_list) == len(years), "The animation should have the same number of frames as data points."
    for frame_artists in lt.artists_list:
        assert len(frame_artists) == 2, "Each frame should contain a scatter plot and a line."
        assert isinstance(frame_artists[1], plt.Line2D), "Second element in frame should be a line."
    plt.close()
    remove(output_file)
