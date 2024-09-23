def zip_lists(list1, list2):
    """Zips two lists together."""
    return [pair for pair in zip(list1, list2)]


def unzip_pairs(pairs):
    """Unzips a list of pairs into two separate lists."""
    return zip(*pairs)



def add(a, b):
    """Adds two numbers."""
    return a + b



def doubler(f):
    """Returns a new function that for any input returns twice the value of f."""
    def g(x):
        return 2 * f(x)
    return g


# Function that prints args and kwargs
def magic(*args, **kwargs):
    """Prints unnamed and keyword arguments."""
    print("unnamed args:", args)
    print("keyword args:", kwargs)

# Function that takes arbitrary arguments and returns the sum
def other_way_magic(x, y, z):
    """Adds three numbers."""
    return x + y + z


# Correct doubler function that works with any number of arguments
def doubler_correct(f):
    """Returns a new function that doubles the output of f, regardless of its arguments."""
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g
