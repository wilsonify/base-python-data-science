import pytest


@pytest.fixture
def naive_square():
    def square(x):
        return x * x

    return square


@pytest.fixture
def naive_square_comprehension():
    def square(x):
        return [_ * _ for _ in x]

    return square


@pytest.fixture
def friendships():
    friendships = [
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]  # user 9
    return friendships
