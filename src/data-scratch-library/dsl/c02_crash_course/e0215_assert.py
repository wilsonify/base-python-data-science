def smallest_item(xs):
    return min(xs)


def smallest_item_guarded(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)
