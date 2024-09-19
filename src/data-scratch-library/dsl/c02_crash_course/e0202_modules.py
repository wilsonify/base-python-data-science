import re
from collections import defaultdict, Counter

import matplotlib.pyplot as plt


def compile_regex(pattern, flags=re.I):
    """
    Compiles a regex pattern with optional flags and returns the compiled object.
    """
    return re.compile(pattern, flags)


def compile_regex_with_alias(pattern, flags=re.I):
    """
    Compiles a regex pattern using an alias for the re module and returns the compiled object.
    """
    import re as regex
    return regex.compile(pattern, flags)


def plot_with_pyplot():
    """
    Creates a simple plot using matplotlib's pyplot module.
    Returns the figure object to allow testable interactions with it.
    """
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    return fig


def create_defaultdict():
    """
    Creates and returns a defaultdict with int as the default factory.
    """
    return defaultdict(int)


def create_counter():
    """
    Creates and returns a Counter object.
    """
    return Counter()
