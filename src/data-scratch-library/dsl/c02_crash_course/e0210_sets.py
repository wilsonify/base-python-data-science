def create_set_with_elements(elements):
    """Creates a set from the given list of elements."""
    return set(elements)

def add_elements_to_set(s, elements):
    """Adds elements to a set."""
    for element in elements:
        s.add(element)
    return s

def is_element_in_set(s, element):
    """Checks if an element is in the set."""
    return element in s

def get_set_length(s):
    """Returns the number of elements in the set."""
    return len(s)

def get_distinct_items(elements):
    """Returns a set of distinct items from the list of elements."""
    return set(elements)

def convert_set_to_list(s):
    """Converts a set to a list."""
    return list(s)
