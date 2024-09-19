import logging

from dsl.c01_intro.introduction import (
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

big_data_str = "Big Data"
interests_list = [
    (0, "Hadoop"),
    (0, big_data_str),
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
    (8, big_data_str),
    (8, "artificial intelligence"),
    (9, "Hadoop"),
    (9, "Java"),
    (9, "MapReduce"),
    (9, big_data_str),
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


def test_friends_of_friend_ids():
    populate_friendships(friendships, users_list)
    read_avg_connections(users_list)
    create_users_by_interest(interests_list)
    create_interests_by_user(interests_list)
    read_num_friends_by_id(users_list)
    result = friends_of_friend_ids(users_list[3])
    assert result == {0: 2, 5: 1}


def test_friends_of_friend_ids_bad():
    logging.info("%r", f"friends of friends bad for user 0: {friends_of_friend_ids_bad(users_list[0])}")


def test_read_most_common_words():
    words_and_counts = create_words_and_counts(interests_list)
    read_most_common_words(words_and_counts)


def test_read_num_friends_by_id():
    read_num_friends_by_id(users_list)


def test_create_words_and_counts():
    words_and_counts = create_words_and_counts(interests_list)
    assert words_and_counts == {
        'big': 3, 'data': 3, 'java': 3, 'python': 3, 'learning': 3, 'hadoop': 2, 'hbase': 2, 'cassandra': 2,
        'scikit-learn': 2, 'r': 2, 'statistics': 2, 'regression': 2, 'probability': 2, 'machine': 2, 'neural': 2,
        'networks': 2, 'spark': 1, 'storm': 1, 'nosql': 1, 'mongodb': 1, 'postgres': 1, 'scipy': 1, 'numpy': 1,
        'statsmodels': 1, 'pandas': 1, 'decision': 1, 'trees': 1, 'libsvm': 1, 'c++': 1, 'haskell': 1, 'programming': 1,
        'languages': 1, 'mathematics': 1, 'theory': 1, 'mahout': 1, 'deep': 1, 'artificial': 1, 'intelligence': 1,
        'mapreduce': 1}


def test_create_average_salary_by_bucket():
    average_salary_by_bucket = create_average_salary_by_bucket(salaries_and_tenures)
    logging.info("%r", f"average salary by tenure bucket {average_salary_by_bucket}")


def test_create_average_salary_by_tenure():
    salary_by_tenure = create_salary_by_tenure(salaries_and_tenures)
    average_salary_by_tenure = create_average_salary_by_tenure(salary_by_tenure)
    logging.info("%r", f"average salary by tenure {average_salary_by_tenure}")


def test_create_salary_by_tenure():
    salary_by_tenure = create_salary_by_tenure(salaries_and_tenures)
    assert salary_by_tenure == {
        0.7: [48000], 1.9: [48000], 2.5: [60000], 4.2: [63000], 6: [76000], 6.5: [69000], 7.5: [76000], 8.1: [88000],
        8.7: [83000], 10: [83000]}


def test_create_interests_by_user():
    create_interests_by_user(interests_list)


def test_create_users_by_interest():
    create_users_by_interest(interests_list)


def test_read_avg_connections():
    read_avg_connections(users_list)


def test_populate_friendships():
    populate_friendships(friendships, users_list)
    assert len(users_list) == 11
