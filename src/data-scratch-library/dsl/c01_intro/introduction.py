"""
"""
import logging
from collections import Counter, defaultdict


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
    """
    how many friends does _user have?
    length of friend_ids list
    """
    return len(_user["friends"])


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


def data_scientists_who_like(target_interest, interests_list):
    return [
        user_id_
        for user_id_, user_interest in interests_list
        if user_interest == target_interest
    ]


def most_common_interests_with(user_id, interests_by_user_id, user_ids_by_interest):
    return Counter(
        interested_user_id
        for interest_ in interests_by_user_id["user_id"]
        for interested_user_id in user_ids_by_interest[interest_]
        if interested_user_id != user_id
    )


def read_most_common_words(words_and_counts):
    logging.info("MOST COMMON WORDS")
    for word, count in words_and_counts.most_common():
        if count > 1:
            logging.info("%r", "word {}, count {}".format(word, count))


def read_num_friends_by_id(users_list):
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


def create_words_and_counts(interests_list):
    words_and_counts = Counter(
        word for user, _interest in interests_list for word in _interest.lower().split()
    )
    return words_and_counts


def create_average_salary_by_bucket(salaries_and_tenures):
    salary_by_tenure_bucket = defaultdict(list)
    for salary, _tenure in salaries_and_tenures:
        bucket = tenure_bucket(_tenure)
        salary_by_tenure_bucket[bucket].append(salary)
    average_salary_by_bucket = {
        tenure_bucket_: sum(salaries) / len(salaries)
        for tenure_bucket_, salaries in salary_by_tenure_bucket.items()
    }
    return average_salary_by_bucket


def create_average_salary_by_tenure(salary_by_tenure):
    average_salary_by_tenure = {
        tenure: sum(salaries) / len(salaries)
        for tenure, salaries in salary_by_tenure.items()
    }
    return average_salary_by_tenure


def create_salary_by_tenure(salaries_and_tenures):
    # keys are years
    # values are the salaries for each tenure
    salary_by_tenure = defaultdict(list)
    for salary, _tenure in salaries_and_tenures:
        salary_by_tenure[_tenure].append(salary)
    return salary_by_tenure


def create_interests_by_user(interests_list):
    # keys are user_ids, values are lists of interests in that user_id
    interests_by_user_id = defaultdict(list)
    for _user_id, interest in interests_list:
        interests_by_user_id[_user_id].append(interest)


def create_users_by_interest(interests_list):
    # keys are interests, values are lists of user_ids with that interest
    user_ids_by_interest = defaultdict(list)
    for _user_id, interest in interests_list:
        user_ids_by_interest[interest].append(_user_id)


def read_avg_connections(users_list):
    num_users = len(users_list)
    total_connections = sum(number_of_friends(user) for user in users_list)  # 24
    avg_connections = total_connections / num_users  # 2.4
    logging.info("%r", f"avg_connections = {avg_connections}")
    logging.info("%r", "total connections {}".format(total_connections))
    logging.info("%r", "number of users {}".format(num_users))
    logging.info("%r", "average connections {}".format(total_connections / num_users))


def read_user_connections(users_list, uid=3):
    friends_of_friend_ids_3 = friends_of_friend_ids(users_list[uid])
    logging.info("%r", f"friends_of_friend_ids_{uid} = {friends_of_friend_ids_3}")  # Counter({0: 2, 5: 1})


def populate_friendships(friendships, users_list):
    # first give each user an empty list
    for user in users_list:
        # noinspection PyTypeChecker
        user["friends"] = []
    # and then populate the lists with friendships
    for i, j in friendships:
        # this works because users[i] is the user whose id is i
        users_list[i]["friends"].append(users_list[j])  # add i as a friend of j
        users_list[j]["friends"].append(users_list[i])  # add j as a friend of i
