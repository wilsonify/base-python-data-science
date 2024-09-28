"""
you want to identify who the “key connectors” are among data scientists.
this data consists of a list of users, each represented by a
dict that contains that user’s id (which is a number) and name
which, in one of the great cosmic coincidences, rhymes with the user’s id:
"""
import logging
from logging.config import dictConfig
from os.path import abspath, dirname

from dsl import logging_config_dict
from dsl.c01_intro import Network


def main():
    network = Network.from_json(abspath(f"{dirname(__file__)}/../../../../data/network.json"))
    logging.info("setup data")
    logging.info("start FINDING KEY CONNECTORS")
    network.populate_friendships()
    network.read_avg_connections()
    network.create_users_by_interest()
    network.create_interests_by_user()
    network.create_words_and_counts()
    network.read_num_friends_by_id()
    logging.info("DATA SCIENTISTS YOU MAY KNOW")
    logging.info("done FINDING KEY CONNECTORS")

    logging.info("%r", f"friends of friends for user 3: {network.users[3].friends_of_friend_ids()}")

    logging.info("start analyzing salary")
    network.create_salary_by_tenure()
    average_salary_by_tenure = network.create_average_salary_by_tenure()
    average_salary_by_bucket = network.create_average_salary_by_bucket()
    logging.info("done analyzing salary")
    logging.info("%r", f"average salary by tenure {average_salary_by_tenure}")
    logging.info("%r", f"average salary by tenure bucket {average_salary_by_bucket}")
    network.read_most_common_words()


if __name__ == "__main__":
    dictConfig(logging_config_dict)
    main()
