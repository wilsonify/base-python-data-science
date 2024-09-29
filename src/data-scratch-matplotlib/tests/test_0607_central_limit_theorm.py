import math

import pytest
from matplotlib import pyplot as plt

from data_plots_from_scratch.c06_probability.e0607_central_limit_theorm import ApproximateNormalHistogram
from dsl.c06_probability.e0603_normal import normal_cdf


@pytest.fixture
def mock_data():
    """Fixture to generate a small set of binomial data for testing."""
    return ApproximateNormalHistogram.generate_binomial_data(0.5, 10, 1000)


def test_generate_binomial_data_length(mock_data):
    """Test that the lengths of the bar_x and bar_y match the number of unique data points."""
    assert len(mock_data.bar_x) == len(mock_data.bar_y)
    assert len(mock_data.plot_xs) == len(mock_data.plot_ys)


def test_generate_binomial_data_normal_approximation(mock_data):
    """Test that the generated normal approximation is valid."""
    mu = 0.5 * 10
    sigma = math.sqrt(10 * 0.5 * (1 - 0.5))

    for i, (plot_x, plot_y) in enumerate(zip(mock_data.plot_xs, mock_data.plot_ys)):
        normal_prob = normal_cdf(plot_x + 0.5, mu, sigma) - normal_cdf(plot_x - 0.5, mu, sigma)
        assert math.isclose(plot_y, normal_prob, rel_tol=1e-2), f"Mismatch at index {i}"


def test_histogram_plot_creation(mock_data, tmpdir):
    """Test that the plot is created and saved correctly."""
    save_path = tmpdir.join("test_binomial_histogram.png")

    # Run the method that generates and saves the plot
    mock_data.binomial_histogram(save_path)

    # Check that the plot was saved
    assert save_path.check(), "Plot was not saved correctly."


def test_plot_closes_after_creation(mock_data, tmpdir):
    """Test that the plot is closed properly after being saved."""
    save_path = tmpdir.join("test_closing_plot.png")

    # Count the number of open figures before the plot is created
    before_plot_count = plt.get_fignums()

    # Run the method that generates and saves the plot
    mock_data.binomial_histogram(save_path)

    # Count the number of open figures after the plot
    after_plot_count = plt.get_fignums()

    # Ensure that no additional figures remain open
    assert len(after_plot_count) == len(before_plot_count), "Figure was not closed properly."


if __name__ == "__main__":
    pytest.main()
