import random
from typing import List

from matplotlib import pyplot as plt

from dsl.c06_probability.e0603_normal import inverse_normal_cdf
from dsl.c10_working_with_data.e1001_univariate import make_histogram


def plot_histogram(points: List[float], bucket_size: float, title: str = ""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)


if __name__ == "__main__":
    random.seed(0)
    # uniform between -100 and 100
    uniform = [200 * random.random() - 100 for _ in range(10000)]

    # normal distribution with mean 0, standard deviation 57
    normal = [
        57 * inverse_normal_cdf(random.random())
        for _ in range(10000)
    ]

    plot_histogram(uniform, 10, "Uniform Histogram")
    plt.savefig("uniform-histogram.png")
    plt.close()

    plot_histogram(normal, 10, "Normal Histogram")
    plt.savefig("normal-histogram.png")
    plt.close()
