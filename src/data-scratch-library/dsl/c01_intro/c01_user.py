from collections import Counter
from dataclasses import dataclass, field


@dataclass
class User:
    id: int
    name: str
    friends: list = field(default_factory=list)

    def number_of_friends(self):
        """
        how many friends does _user have?
        length of friend_ids list
        """
        return len(self.friends)

    def friends_of_friend_ids(self):
        return Counter(
            foaf.id  # Access the id directly from the User object
            for friend in self.friends  # For each of my friends
            for foaf in friend.friends  # Count *their* friends
            if self.not_the_same(foaf) and self.not_friends(foaf)  # Who aren't me and aren't my friends
        )

    def not_the_same(self, other_user: 'User'):
        """
        two users are not the same if they have different ids
        interpret the string 'User' as a type reference to this class,
        even though it hasn't been fully defined yet.
        """
        return self.id != other_user.id

    def not_friends(self, other_user: 'User'):
        """other_user is not a friend if he's not in user["friends"];
        that is, if he's not_the_same as all the people in user["friends"]"""
        return all(other_user.not_the_same(friend) for friend in self.friends)
