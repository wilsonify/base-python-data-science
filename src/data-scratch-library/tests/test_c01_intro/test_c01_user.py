from dsl.c01_intro import User


def test_not_the_same():
    user_a = User(id=1, name='Alice')
    user_b = User(id=2, name='Bob')
    assert user_a.not_the_same(user_b)


def test_not_friends():
    user_a = User(id=1, name='Alice')
    user_b = User(id=2, name='Bob')
    assert user_a.not_friends(user_b)


def test_no_friends():
    user_a = User(id=1, name='Alice')
    assert user_a.number_of_friends() == 0  # Alice has no friends


def test_number_of_friends():
    user_a = User(id=1, name='Alice')
    user_b = User(id=2, name='Bob')
    user_c = User(id=3, name='Charlie')
    user_a.friends = [user_b, user_c]  # Alice is friends with Bob and Charlie
    assert user_a.number_of_friends() == 2  # Alice has 2 friends


if __name__ == "__main__":
    from test_runner import TestRunner
    runner = TestRunner()
    runner.run_file(__file__)
