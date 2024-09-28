from dsl.c01_intro import Interest


def test_interest_creation():
    # Create an interest instance
    interest = Interest(user_id=1, interest='Reading')

    # Check that the attributes are set correctly
    assert interest.user_id == 1
    assert interest.interest == 'Reading'


def test_interest_equality():
    interest1 = Interest(user_id=1, interest='Reading')
    interest2 = Interest(user_id=1, interest='Reading')
    interest3 = Interest(user_id=2, interest='Reading')
    interest4 = Interest(user_id=1, interest='Traveling')

    # Test that two interests with the same attributes are considered equal
    assert interest1 == interest2

    # Test that interests with different user IDs are not equal
    assert interest1 != interest3

    # Test that interests with different interests are not equal
    assert interest1 != interest4
