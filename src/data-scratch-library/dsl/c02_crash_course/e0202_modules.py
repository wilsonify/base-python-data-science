import re
from collections import defaultdict, Counter




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
