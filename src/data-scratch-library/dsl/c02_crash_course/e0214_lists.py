def get_even_numbers(n):
    """Returns a list of even numbers up to n."""
    return [x for x in range(n) if x % 2 == 0]

def get_square_dict(n):
    """Returns a dictionary mapping numbers to their squares up to n."""
    return {x: x * x for x in range(n)}

def get_increasing_pairs(n):
    """Returns all pairs (x, y) where x < y for x, y in range(n)."""
    return [(x, y) for x in range(n) for y in range(x + 1, n)]
