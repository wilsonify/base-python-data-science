from collections import Counter
from os import remove
from os.path import abspath, dirname

import pytest

from dsl.c01_intro import User, Friendship, Interest, Network
from dsl.c01_intro.c04_salary_from_tenure import SalaryTenure


@pytest.fixture(name="network01")
def network01_fixture():
    return Network(
        users=[User(id=i, name=f"User {i}") for i in range(3)],
        friendships=[
            Friendship(user1_id=0, user2_id=1),
            Friendship(user1_id=1, user2_id=2)
        ],
        interests=[
            Interest(user_id=0, interest="Python"),
            Interest(user_id=1, interest="Data Science"),
            Interest(user_id=1, interest="Python"),
            Interest(user_id=2, interest="Machine Learning"),
        ],
        salaries_and_tenures=[
            SalaryTenure(salary=50000, tenure=2.5),
            SalaryTenure(salary=70000, tenure=3.0),
            SalaryTenure(salary=90000, tenure=8.0),
        ]
    )


def test_populate_friendships(network01):
    network01.populate_friendships()
    # Check that friends have been populated correctly
    assert len(network01.users[0].friends) == 1  # User 0 has one friend (User 1)
    assert len(network01.users[1].friends) == 2  # User 1 has two friends (User 0 and User 2)
    assert len(network01.users[2].friends) == 1  # User 2 has one friend (User 1)


def test_read_avg_connections(network01):
    network01.populate_friendships()
    network01.read_avg_connections()


def test_create_users_by_interest(network01):
    # Check user_ids_by_interest
    network01.create_users_by_interest()
    expected = {
        "Python": [0, 1],
        "Data Science": [1],
        "Machine Learning": [2],
    }
    assert network01.user_ids_by_interest == expected


def test_create_interests_by_user(network01):
    # Check interests_by_user_id
    network01.create_interests_by_user()
    expected = {
        0: ["Python"],
        1: ["Data Science", "Python"],
        2: ["Machine Learning"],
    }
    assert network01.interests_by_user_id == expected


def test_create_salary_by_tenure(network01):
    network01.create_salary_by_tenure()
    expected = {
        2.5: [50000],
        3.0: [70000],
        8.0: [90000],
    }
    assert dict(network01.salary_by_tenure) == expected


def test_create_average_salary_by_tenure(network01):
    # Check average salary by tenure
    network01.create_salary_by_tenure()
    avg_salary = network01.create_average_salary_by_tenure()
    expected = {
        2.5: 50000.0,
        3.0: 70000.0,
        8.0: 90000.0,
    }
    assert avg_salary == expected


def test_data_scientists_who_like(network01):
    result = network01.data_scientists_who_like("Python")
    # User 0 and User 1 like Python
    assert result == [0, 1]


def test_most_common_interests_with(network01):
    # Check common interests excluding User 1
    # User 0 has "Python", User 2 has "Machine Learning"
    network01.create_interests_by_user()
    network01.create_users_by_interest()
    result = network01.most_common_interests_with(user_id=1)
    expected = Counter({0: 1, 2: 0})
    assert result == expected


def test_create_words_and_counts(network01):
    # Check word counts from interests
    network01.create_words_and_counts()
    expected = Counter({
        "python": 2,
        "data": 1,
        "science": 1,
        "machine": 1,
        "learning": 1
    })
    assert network01.words_and_counts == expected


def test_read_most_common_words(network01):
    network01.create_words_and_counts()
    network01.read_most_common_words()


def test_create_average_salary_by_bucket(network01):
    avg_salary_by_bucket = network01.create_average_salary_by_bucket()
    expected = {'between two and five': 60000.0, 'more than five': 90000.0}
    assert avg_salary_by_bucket == expected


def test_read_num_friends_by_id(network01):
    network01.populate_friendships()
    network01.read_num_friends_by_id()


def test_read_user_connections(network01):
    network01.populate_friendships()
    network01.read_user_connections(uid=1)


def test_from_json(network01):

    in_json_file_path = abspath(f"{dirname(__file__)}/../../../../data/example_network.json")
    loaded_network = Network.from_json(in_json_file_path)
    assert loaded_network.users == [User(id=0, name='User 0', friends=[]), User(id=1, name='User 1', friends=[]),
                                    User(id=2, name='User 2', friends=[])]
    assert loaded_network.friendships == [Friendship(user1_id=0, user2_id=1), Friendship(user1_id=1, user2_id=2)]
    assert loaded_network.interests == [Interest(user_id=0, interest='Python'),
                                        Interest(user_id=1, interest='Data Science'),
                                        Interest(user_id=1, interest='Python'),
                                        Interest(user_id=2, interest='Machine Learning')]
    assert loaded_network.salaries_and_tenures == [SalaryTenure(salary=50000, tenure=2.5),
                                                   SalaryTenure(salary=70000, tenure=3.0),
                                                   SalaryTenure(salary=90000, tenure=8.0)]


def test_to_json(network01):
    network01.to_json("network.out.json")
    remove("network.out.json")
