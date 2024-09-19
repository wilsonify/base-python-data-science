def sort_list(lst, reverse=False):
    """Sorts a list in place or returns a sorted copy."""
    if reverse:
        return sorted(lst, reverse=True)
    return sorted(lst)

def sort_by_key(items, key_func, reverse=False):
    """Sorts items by a custom key function."""
    return sorted(items, key=key_func, reverse=reverse)
