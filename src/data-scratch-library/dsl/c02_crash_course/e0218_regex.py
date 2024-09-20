import re



def zip_lists(list1, list2):
    """Zips two lists together."""
    return [pair for pair in zip(list1, list2)]



def unzip_pairs(pairs):
    """Unzips a list of pairs into two separate lists."""
    return zip(*pairs)


# Function to add two numbers
def add(a, b):
    """Adds two numbers."""
    return a + b


