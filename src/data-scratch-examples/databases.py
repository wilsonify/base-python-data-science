import logging
from logging.config import dictConfig

from dsl.databases import Table


def main():
    users = Table(["user_id", "name", "num_friends"])
    users.insert([0, "Hero", 0])
    users.insert([1, "Dunn", 2])
    users.insert([2, "Sue", 3])
    users.insert([3, "Chi", 3])
    users.insert([4, "Thor", 3])
    users.insert([5, "Clive", 2])
    users.insert([6, "Hicks", 3])
    users.insert([7, "Devin", 2])
    users.insert([8, "Kate", 2])
    users.insert([9, "Klein", 3])
    users.insert([10, "Jen", 1])

    logging.info("%r", "users = {}".format(users))

    # SELECT

    logging.info("%r", "users.select() = {}".format(users.select()))

    limited_users = users.limit(2)
    logging.info("%r", "limited_users = {}".format(limited_users))

    selected_users = users.select(keep_columns=["user_id"])
    logging.info("%r", "selected_users = {}".format(selected_users))

    users_named_dunn = users.where(lambda row: row["name"] == "Dunn").select(
        keep_columns=["user_id"]
    )
    logging.info("%r", "users_named_dunn = {}".format(users_named_dunn))

    def name_len(row):
        return len(row["name"])

    user_with_name_length = users.select(
        keep_columns=[], additional_columns={"name_length": name_len}
    )
    logging.debug("name_len = {}".format(name_len))
    logging.info("%r", "user_with_name_length = {}".format(user_with_name_length))

    def min_user_id(rows):
        return min(row["user_id"] for row in rows)

    stats_by_length = users.select(additional_columns={"name_len": name_len}).group_by(
        group_by_columns=["name_len"],
        aggregates={"min_user_id": min_user_id, "num_users": len},
    )

    logging.info("%r", "stats_by_length = {}".format(stats_by_length))

    def first_letter_of_name(row):
        return row["name"][0] if row["name"] else ""

    def average_num_friends(rows):
        return sum(row["num_friends"] for row in rows) / len(rows)

    def enough_friends(rows):
        return average_num_friends(rows) > 1

    avg_friends_by_letter = users.select(
        additional_columns={"first_letter": first_letter_of_name}
    ).group_by(
        group_by_columns=["first_letter"],
        aggregates={"avg_num_friends": average_num_friends},
        having=enough_friends,
    )

    logging.info("%r", "avg_friends_by_letter = {}".format(avg_friends_by_letter))

    def sum_user_ids(rows):
        return sum(row["user_id"] for row in rows)

    user_id_sum = users.where(lambda row: row["user_id"] > 1).group_by(
        group_by_columns=[], aggregates={"user_id_sum": sum_user_ids}
    )

    logging.info("%r", "user_id_sum = {}".format(user_id_sum))

    # ORDER BY

    friendliest_letters = avg_friends_by_letter.order_by(
        lambda row: -row["avg_num_friends"]
    ).limit(4)

    logging.info("%r", "friendliest_letters = {}".format(friendliest_letters))

    # JOINs

    user_interests = Table(["user_id", "interest"])
    user_interests.insert([0, "SQL"])
    user_interests.insert([0, "NoSQL"])
    user_interests.insert([2, "SQL"])
    user_interests.insert([2, "MySQL"])

    # noinspection PyPep8
    sql_users = (
        users.join(user_interests)
        .where(lambda row: row["interest"] == "SQL")
        .select(keep_columns=["name"])
    )

    logging.info("%r", "sql_users = {}".format(sql_users))

    def count_interests(rows):
        """counts how many rows have non-None interests"""
        return len([row for row in rows if row["interest"] is not None])

    user_interest_counts = users.join(user_interests, left_join=True).group_by(
        group_by_columns=["user_id"], aggregates={"num_interests": count_interests}
    )

    logging.info("%r", "user interest counts = {}".format(user_interest_counts))

    # SUBQUERIES

    likes_sql_user_ids = user_interests.where(
        lambda row: row["interest"] == "SQL"
    ).select(keep_columns=["user_id"])

    likes_sql_user_ids.group_by(
        group_by_columns=[], aggregates={"min_user_id": min_user_id}
    )

    logging.info("%r", "likes sql user ids = {}".format(likes_sql_user_ids))


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
