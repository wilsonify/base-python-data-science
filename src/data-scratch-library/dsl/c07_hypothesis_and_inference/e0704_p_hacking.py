"""
P-hacking
A procedure that erroneously rejects the null hypothesis only 5% of the time
will—by definition—5% of the time erroneously reject the null hypothesis.
"""

import random


def run_experiment():
    """flip a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiment):
    """using the 5% significance levels"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531


def main():
    random.seed(0)
    experiments = [run_experiment() for _ in range(1000)]
    num_rejections = len([experiment
                          for experiment in experiments
                          if reject_fairness(experiment)])
    assert num_rejections == 46


if __name__ == "__main__":
    main()
