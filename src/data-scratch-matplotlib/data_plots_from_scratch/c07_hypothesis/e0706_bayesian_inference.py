import matplotlib.pyplot as plt
import numpy as np

from dsl.c07_hypothesis_and_inference.e0706_bayesian_inference import beta_pdf


def plot_beta_distributions(distributions):
    # Values for x in [0, 1] range
    x = np.linspace(0, 1, 100)

    # Plotting
    plt.figure(figsize=(10, 6))

    for dist in distributions:
        alpha, beta, label = dist["alpha"], dist["beta"], dist["label"]
        y = [beta_pdf(xi, alpha, beta) for xi in x]
        plt.plot(x, y, label=label)

    plt.title("Beta Distributions")
    plt.xlabel("x")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.grid(True)



if __name__ == "__main__":
    # Beta distribution parameters
    distributions = [
        {"alpha": 1, "beta": 1, "label": "Beta(1,1)"},
        {"alpha": 10, "beta": 10, "label": "Beta(10,10)"},
        {"alpha": 4, "beta": 16, "label": "Beta(4,16)"},
        {"alpha": 16, "beta": 4, "label": "Beta(16,4)"}
    ]
    plot_beta_distributions(distributions)
    plt.savefig("e0706_beta_distributions.png")

    distributions = [
        {"alpha": 4, "beta": 8, "label": "Beta(4,8)"},
        {"alpha": 23, "beta": 27, "label": "Beta(23,27)"},
        {"alpha": 33, "beta": 17, "label": "Beta(33,17)"}
    ]
    plot_beta_distributions(distributions)
    plt.savefig("e0706_beta_distributions_coins.png")
