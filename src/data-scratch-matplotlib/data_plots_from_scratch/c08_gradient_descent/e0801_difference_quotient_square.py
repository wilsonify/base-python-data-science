import logging
from logging.config import dictConfig

from dsl.c08_gradient_descent.e0801_estimating_gradient import difference_quotient


def square(x: float) -> float:
    return x * x


def derivative_square(x: float) -> float:
    return 2 * x


def main():
    logging.info("using the gradient")
    xs = range(-10, 11)
    actuals = [derivative_square(x) for x in xs]
    estimates = [difference_quotient(square, x, h=0.001) for x in xs]
    # plot to show they're basically the same
    import matplotlib.pyplot as plt
    plt.title("Actual Derivatives vs. Estimates")
    plt.plot(xs, actuals, 'rx', label='Actual')
    plt.plot(xs, estimates, 'b+', label='Estimate')
    plt.legend(loc=9)
    plt.show()


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
