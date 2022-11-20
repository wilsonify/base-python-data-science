"""
"""
import logging
from collections import Counter, defaultdict
from logging.config import dictConfig

from dsl import config


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


def number_of_friends(_user):
    """how many friends does _user_ have?"""
    return len(_user["friends"])  # length of friend_ids list


def friends_of_friend_ids_bad(user_):
    # "foaf" is short for "friend of a friend"
    return [
        foaf["id"]
        for friend in user_["friends"]  # for each of user's friends
        for foaf in friend["friends"]
    ]  # get each of _their_ friends


def not_the_same(user_, other_user):
    """two users are not the same if they have different ids"""
    return user_["id"] != other_user["id"]


def not_friends(user_, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user) for friend in user_["friends"])


def friends_of_friend_ids(user_):
    return Counter(
        foaf["id"]
        for friend in user_["friends"]  # for each of my friends
        for foaf in friend["friends"]  # count *their* friends
        if not_the_same(user_, foaf) and not_friends(user_, foaf)  # who aren't me
    )  # and aren't my friends


def data_scientists_who_like(target_interest,interests_list):
    return [
        user_id_
        for user_id_, user_interest in interests_list
        if user_interest == target_interest
    ]


def most_common_interests_with(user_id,interests_by_user_id,user_ids_by_interest):
    return Counter(
        interested_user_id
        for interest_ in interests_by_user_id["user_id"]
        for interested_user_id in user_ids_by_interest[interest_]
        if interested_user_id != user_id
    )


def main():
    logging.info("setup data")
    users_list = [
        {"id": 0, "name": "Hero"},
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {"id": 4, "name": "Thor"},
        {"id": 5, "name": "Clive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Klein"},
        {"id": 10, "name": "Jen"},
    ]

    friendships = [
        (0, 1),
        (0, 2),
        (1, 2),
        (1, 3),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (5, 7),
        (6, 8),
        (7, 8),
        (8, 9),
    ]

    # first give each user an empty list
    for user in users_list:
        # noinspection PyTypeChecker
        user["friends"] = []

    # and then populate the lists with friendships
    for i, j in friendships:
        # this works because users[i] is the user whose id is i
        users_list[i]["friends"].append(users_list[j])  # add i as a friend of j
        users_list[j]["friends"].append(users_list[i])  # add j as a friend of i

    total_connections = sum(number_of_friends(user) for user in users_list)  # 24

    num_users = len(users_list)
    avg_connections = total_connections / num_users  # 2.4

    friends_of_friend_ids_3 = friends_of_friend_ids(users_list[3])
    logging.info("%r", "friends_of_friend_ids_3 = {}".format(friends_of_friend_ids_3))  # Counter({0: 2, 5: 1})

    interests_list = [
        (0, "Hadoop"),
        (0, "Big Data"),
        (0, "HBase"),
        (0, "Java"),
        (0, "Spark"),
        (0, "Storm"),
        (0, "Cassandra"),
        (1, "NoSQL"),
        (1, "MongoDB"),
        (1, "Cassandra"),
        (1, "HBase"),
        (1, "Postgres"),
        (2, "Python"),
        (2, "scikit-learn"),
        (2, "scipy"),
        (2, "numpy"),
        (2, "statsmodels"),
        (2, "pandas"),
        (3, "R"),
        (3, "Python"),
        (3, "statistics"),
        (3, "regression"),
        (3, "probability"),
        (4, "machine learning"),
        (4, "regression"),
        (4, "decision trees"),
        (4, "libsvm"),
        (5, "Python"),
        (5, "R"),
        (5, "Java"),
        (5, "C++"),
        (5, "Haskell"),
        (5, "programming languages"),
        (6, "statistics"),
        (6, "probability"),
        (6, "mathematics"),
        (6, "theory"),
        (7, "machine learning"),
        (7, "scikit-learn"),
        (7, "Mahout"),
        (7, "neural networks"),
        (8, "neural networks"),
        (8, "deep learning"),
        (8, "Big Data"),
        (8, "artificial intelligence"),
        (9, "Hadoop"),
        (9, "Java"),
        (9, "MapReduce"),
        (9, "Big Data"),
    ]

    # keys are interests, values are lists of user_ids with that interest
    user_ids_by_interest = defaultdict(list)

    for _user_id, interest in interests_list:
        user_ids_by_interest[interest].append(_user_id)

    # keys are user_ids, values are lists of interests for that user_id
    interests_by_user_id = defaultdict(list)

    for _user_id, interest in interests_list:
        interests_by_user_id[_user_id].append(interest)

    ###########################
    #                         #
    # SALARIES AND EXPERIENCE #
    #                         #
    ###########################

    salaries_and_tenures = [
        (83000, 8.7),
        (88000, 8.1),
        (48000, 0.7),
        (76000, 6),
        (69000, 6.5),
        (76000, 7.5),
        (60000, 2.5),
        (83000, 10),
        (48000, 1.9),
        (63000, 4.2),
    ]

    # keys are years
    # values are the salaries for each tenure
    salary_by_tenure = defaultdict(list)

    for salary, _tenure in salaries_and_tenures:
        salary_by_tenure[_tenure].append(salary)

    average_salary_by_tenure = {
        tenure: sum(salaries) / len(salaries)
        for tenure, salaries in salary_by_tenure.items()
    }

    salary_by_tenure_bucket = defaultdict(list)

    for salary, _tenure in salaries_and_tenures:
        bucket = tenure_bucket(_tenure)
        salary_by_tenure_bucket[bucket].append(salary)

    average_salary_by_bucket = {
        tenure_bucket_: sum(salaries) / len(salaries)
        for tenure_bucket_, salaries in salary_by_tenure_bucket.items()
    }

    words_and_counts = Counter(
        word for user, _interest in interests_list for word in _interest.lower().split()
    )

    logging.info("# FINDING KEY CONNECTORS")

    logging.info("%r", "total connections {}".format(total_connections))
    logging.info("%r", "number of users {}".format(num_users))
    logging.info("%r", "average connections {}".format(total_connections / num_users))

    # create a list (user_id, number_of_friends)
    num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users_list]

    logging.info(
        "%r",
        "users sorted by number of friends: {}".format(
            sorted(
                num_friends_by_id,
                key=lambda pair: pair[1],  # by number of friends
                reverse=True,
            )
        ),
    )  # largest to smallest

    logging.info("DATA SCIENTISTS YOU MAY KNOW")

    logging.info(
        "%r",
        "friends of friends bad for user 0: {}".format(
            friends_of_friend_ids_bad(users_list[0]),
        ),
    )
    logging.info(
        "%r",
        "friends of friends for user 3: {}".format(
            friends_of_friend_ids(users_list[3])
        ),
    )

    logging.info("# SALARIES AND TENURES")

    logging.info("%r", "average salary by tenure {}".format(average_salary_by_tenure))
    logging.info(
        "%r", "average salary by tenure bucket {}".format(average_salary_by_bucket)
    )

    logging.info("MOST COMMON WORDS")

    for word, count in words_and_counts.most_common():
        if count > 1:
            logging.info("%r", "word {}, count {}".format(word, count))


if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)
    main()
