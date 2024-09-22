from data_plots_from_scratch.visualizing_data import plot_with_pyplot


def test_plot_with_pyplot():
    fig = plot_with_pyplot()
    assert fig is not None
    assert hasattr(fig, 'axes')
    assert len(fig.axes) > 0
