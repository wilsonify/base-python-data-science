from dsl.c01_intro import Friendship


def test_friendship_creation():
    # Create two friendship instances
    friendship = Friendship(user1_id=1, user2_id=2)

    # Check that the attributes are set correctly
    assert friendship.user1_id == 1
    assert friendship.user2_id == 2


def test_friendship_equality():
    friendship1 = Friendship(user1_id=1, user2_id=2)
    friendship2 = Friendship(user1_id=1, user2_id=2)
    friendship3 = Friendship(user1_id=2, user2_id=1)

    # Test that two friendships with the same IDs are considered equal
    assert friendship1 == friendship2

    # Test that friendships with different user IDs are not equal
    assert friendship1 != friendship3
