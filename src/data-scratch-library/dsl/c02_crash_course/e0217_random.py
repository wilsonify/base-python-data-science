import random


def generate_uniform_randoms(seed, n):
    """
    Generates a list of `n` random numbers between 0 and 1 using a given seed.
    """
    random.seed(seed)
    return [random.random() for _ in range(n)]


def random_from_range(seed, start, end=None):
    """
    generating a random number from a range
    Returns a random number from a given range.
    If only one argument is provided, the range will be from 0 to start-1.
    """
    random.seed(seed)
    if end is None:
        return random.randrange(start)
    return random.randrange(start, end)


def shuffle_list(seed, items):
    """Shuffles a given list using a seed."""
    random.seed(seed)
    random.shuffle(items)
    return items


def random_choice(seed, items):
    """Returns a random element from a given list."""
    random.seed(seed)
    return random.choice(items)


def random_sample(seed, items, n):
    """Returns a random sample of `n` elements from a given list without replacement."""
    random.seed(seed)
    return random.sample(items, n)


def random_choice_with_replacement(seed, items, n):
    """Returns a list of `n` random elements from a given list with replacement."""
    random.seed(seed)
    return [random.choice(items) for _ in range(n)]

