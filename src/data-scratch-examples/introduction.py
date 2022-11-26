import logging
from logging.config import dictConfig

from dsl.introduction import (
    friends_of_friend_ids,
    friends_of_friend_ids_bad,
    read_most_common_words,
    read_num_friends_by_id,
    create_words_and_counts,
    create_average_salary_by_bucket,
    create_average_salary_by_tenure,
    create_salary_by_tenure,
    create_interests_by_user,
    create_users_by_interest,
    read_avg_connections,
    populate_friendships
)

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


def main():
    logging.info("setup data")
    logging.info("start FINDING KEY CONNECTORS")
    populate_friendships(friendships, users_list)
    read_avg_connections(users_list)
    create_users_by_interest(interests_list)
    create_interests_by_user(interests_list)
    words_and_counts = create_words_and_counts(interests_list)
    read_num_friends_by_id(users_list)
    logging.info("DATA SCIENTISTS YOU MAY KNOW")
    logging.info("%r", f"friends of friends bad for user 0: {friends_of_friend_ids_bad(users_list[0])}")
    logging.info("%r", f"friends of friends for user 3: {friends_of_friend_ids(users_list[3])}")
    logging.info("done FINDING KEY CONNECTORS")

    logging.info("start analyzing salary")
    salary_by_tenure = create_salary_by_tenure(salaries_and_tenures)
    average_salary_by_tenure = create_average_salary_by_tenure(salary_by_tenure)
    average_salary_by_bucket = create_average_salary_by_bucket(salaries_and_tenures)
    logging.info("done analyzin salary")
    logging.info("%r", f"average salary by tenure {average_salary_by_tenure}")
    logging.info("%r", f"average salary by tenure bucket {average_salary_by_bucket}")

    read_most_common_words(words_and_counts)


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
