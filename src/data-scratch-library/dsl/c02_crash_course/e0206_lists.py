def list_length(lst):
    """Returns the length of the list."""
    return len(lst)

def list_sum(lst):
    """Returns the sum of the list elements."""
    return sum(lst)

def get_nth_element(lst, n):
    """Returns the nth element of the list (supports negative indexing)."""
    return lst[n]

def slice_list(lst, start=None, end=None, step=None):
    """Returns a slice of the list based on start, end, and step."""
    return lst[start:end:step]

def list_contains(lst, item):
    """Returns True if the list contains the item, False otherwise."""
    return item in lst

def list_extend(lst, items):
    """Extends the list with the items provided."""
    lst.extend(items)
    return lst

def list_append(lst, item):
    """Appends an item to the list."""
    lst.append(item)
    return lst

def unpack_list(lst):
    """Unpacks the first two elements of a list into x and y."""
    if len(lst) != 2:
        raise ValueError("List must contain exactly two elements.")
    x, y = lst
    return x, y
