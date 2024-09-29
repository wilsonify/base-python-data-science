import math
from collections import Counter
from dataclasses import dataclass
from typing import List

from matplotlib import pyplot as plt

from data_plots_from_scratch import initialize_plot
from dsl.c06_probability.e0603_normal import normal_cdf
from dsl.c06_probability.e0604_binom import binomial


@dataclass
class ApproximateNormalHistogram:
    bar_x: List[float]
    bar_y: List[float]
    plot_xs: List[int]
    plot_ys: List[float]

    @classmethod
    def generate_binomial_data(cls, p: float, n: int, num_points: int) -> "ApproximateNormalHistogram":
        """Generates binomial sample data and normal approximation"""
        data = [binomial(n, p) for _ in range(num_points)]

        # Binomial sample histogram
        histogram = Counter(data)
        bar_x = [x - 0.4 for x in histogram.keys()]
        bar_y = [v / num_points for v in histogram.values()]

        # Normal approximation
        mu = p * n
        sigma = math.sqrt(n * p * (1 - p))
        plot_xs = list(range(min(data), max(data) + 1))
        plot_ys = [
            normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in plot_xs
        ]

        return cls(bar_x=bar_x, bar_y=bar_y, plot_xs=plot_xs, plot_ys=plot_ys)

    def binomial_histogram(self, save_path: str) -> None:
        """Plots binomial samples and normal approximation, and saves the plot."""
        fig, ax = initialize_plot()
        ax.bar(self.bar_x, self.bar_y, width=0.8, color='0.75', label="Binomial Samples")
        ax.plot(self.plot_xs, self.plot_ys, color='black', label="Normal Approximation")
        ax.set_title("Binomial Distribution vs. Normal Approximation")
        ax.legend()

        # Save plot
        plt.savefig(save_path)
        plt.close(fig)


if __name__ == "__main__":
    data = ApproximateNormalHistogram.generate_binomial_data(0.75, 100, 10000)
    data.binomial_histogram("e0607_binomial_approximate_normal.png")
