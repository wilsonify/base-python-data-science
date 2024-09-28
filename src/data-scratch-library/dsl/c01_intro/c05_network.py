import json
import logging
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict, field
from typing import List

from dsl.c01_intro import User, Friendship, Interest
from dsl.c01_intro.c04_salary_from_tenure import SalaryTenure


@dataclass
class Network:
    users: list[User]
    friendships: list[Friendship]
    interests: list[Interest]
    salaries_and_tenures: list[SalaryTenure]
    interests_by_user_id: dict[int, List[str]] = field(default_factory=dict)
    user_ids_by_interest: dict[str, List[int]] = field(default_factory=dict)
    words_and_counts: Counter = field(default_factory=Counter)
    average_salary_by_bucket: dict = field(default_factory=dict)
    salary_by_tenure: dict[float, list] = field(default_factory=dict)
    average_salary_by_tenure: dict[float, list] = field(default_factory=dict)

    def populate_friendships(self):
        # First, give each user an empty list for friends
        for user in self.users:
            user.friends = []  # Dynamically add 'friends' attribute

        # Populate the lists with friendships
        for friendship in self.friendships:
            user1 = self.users[friendship.user1_id]  # user with id user1_id
            user2 = self.users[friendship.user2_id]  # user with id user2_id

            user1.friends.append(user2)  # add user2 as a friend of user1
            user2.friends.append(user1)  # add user1 as a friend of user2

    def read_avg_connections(self):
        num_users = len(self.users)
        total_connections = sum(user.number_of_friends() for user in self.users)
        avg_connections = total_connections / num_users
        logging.info("%r", f"avg_connections = {avg_connections}")
        logging.info("%r", "total connections {}".format(total_connections))
        logging.info("%r", "number of users {}".format(num_users))
        logging.info("%r", "average connections {}".format(total_connections / num_users))

    def create_users_by_interest(self):
        # keys are interests, values are lists of user_ids with that interest
        self.user_ids_by_interest = defaultdict(list)
        for interest_obj in self.interests:
            # Append the user_id to the list for the corresponding interest
            self.user_ids_by_interest[interest_obj.interest].append(interest_obj.user_id)

    def create_interests_by_user(self):
        """Populate interests_by_user_id with interests linked to user IDs."""
        self.interests_by_user_id = defaultdict(list)  # Ensure it's instance-specific

        for interest_obj in self.interests:
            self.interests_by_user_id[interest_obj.user_id].append(interest_obj.interest)

    def create_salary_by_tenure(self):
        # keys are years
        # values are the salaries for each tenure
        self.salary_by_tenure = defaultdict(list)
        for salary_tenure in self.salaries_and_tenures:
            self.salary_by_tenure[salary_tenure.tenure].append(salary_tenure.salary)

    def create_average_salary_by_tenure(self):
        self.average_salary_by_tenure = {
            tenure: sum(salaries) / len(salaries)
            for tenure, salaries in self.salary_by_tenure.items()
        }
        return self.average_salary_by_tenure

    def data_scientists_who_like(self, target_interest: str):
        return [
            interest.user_id  # Access user_id from the Interest object
            for interest in self.interests  # Iterate over Interest objects
            if interest.interest == target_interest  # Check if the interest matches
        ]

    def most_common_interests_with(self,user_id):
        return Counter(
            interested_user_id
            for interest in self.interests_by_user_id[user_id]
            for interested_user_id in self.user_ids_by_interest[interest]
            if interested_user_id != user_id
        )

    def create_words_and_counts(self):
        # Create a Counter of words from the interests
        self.words_and_counts = Counter(
            word
            for interest_obj in self.interests
            for word in interest_obj.interest.lower().split()
        )

    def read_most_common_words(self):
        logging.info("MOST COMMON WORDS")
        for word, count in self.words_and_counts.most_common():
            if count > 1:
                logging.info("%r", "word {}, count {}".format(word, count))

    def create_average_salary_by_bucket(self):
        salary_by_tenure_bucket = defaultdict(list)

        for salary_tenure in self.salaries_and_tenures:
            bucket = salary_tenure.tenure_bucket()
            salary_by_tenure_bucket[bucket].append(salary_tenure.salary)  # Access salary attribute

        average_salary_by_bucket = {
            tenure_bucket_: sum(salaries) / len(salaries)
            for tenure_bucket_, salaries in salary_by_tenure_bucket.items()
            if salaries  # Ensure that we only calculate for non-empty lists
        }

        return average_salary_by_bucket

    def read_num_friends_by_id(self):
        # create a list of (user_id, number_of_friends)
        num_friends_by_id = [(user.id, user.number_of_friends()) for user in self.users]

        logging.info(
            "%r",
            "users sorted by number of friends: {}".format(
                sorted(
                    num_friends_by_id,
                    key=lambda pair: pair[1],  # sort by number of friends
                    reverse=True,  # largest to smallest
                )
            ),
        )

    def read_user_connections(self, uid):
        logging.info("%r", f"friends_of_friend_ids_{uid} = {self.users[uid].friends_of_friend_ids()}")

    def to_json(self, path_to_network_dot_json):
        with open(path_to_network_dot_json, "w") as json_file:
            json.dump(asdict(self), json_file)

    @classmethod
    def from_json(cls, path_to_network_dot_json):
        with open(path_to_network_dot_json, "r") as json_file:
            dictionary = json.load(json_file)

        return cls(
            users=[
                User(id=user_dict["id"], name=user_dict["name"]) for user_dict in dictionary["users"]
            ],
            friendships=[
                Friendship(
                    user1_id=friendship_dict["user1_id"],
                    user2_id=friendship_dict["user2_id"]
                ) for friendship_dict in dictionary["friendships"]
            ],
            interests=[
                Interest(
                    user_id=interest_dict["user_id"],
                    interest=interest_dict["interest"]
                ) for interest_dict in dictionary["interests"]
            ],
            salaries_and_tenures=[
                SalaryTenure(
                    salary=salary_tenure_dict["salary"],
                    tenure=salary_tenure_dict["tenure"]
                ) for salary_tenure_dict in dictionary["salaries_and_tenures"]]
        )
