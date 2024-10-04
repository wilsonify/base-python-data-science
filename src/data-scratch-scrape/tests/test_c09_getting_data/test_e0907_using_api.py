# Test functions
from collections import Counter

from data_scrape_from_scratch.c09_getting_data.e0907_using_api import deserialize_json, get_publication_year, \
    get_last_5_repo_languages, fetch_github_repos, count_repos_by_weekday, extract_repo_creation_dates, \
    count_repos_by_month, check_topic_in_json


def test_deserialize_json():
    serialized = """{ "title" : "Data Science Book",
                     "author" : "Joel Grus",
                     "publicationYear" : 2019,
                     "topics" : [ "data", "science", "data science"] }"""
    deserialized = deserialize_json(serialized)
    assert deserialized["title"] == "Data Science Book"
    assert deserialized["author"] == "Joel Grus"


def test_get_publication_year():
    serialized = """{ "title" : "Data Science Book",
                     "author" : "Joel Grus",
                     "publicationYear" : 2019,
                     "topics" : [ "data", "science", "data science"] }"""
    deserialized = deserialize_json(serialized)
    publication_year = get_publication_year(deserialized)
    assert publication_year == 2019


def test_check_topic_in_json():
    serialized = """{ "title" : "Data Science Book",
                     "author" : "Joel Grus",
                     "publicationYear" : 2019,
                     "topics" : [ "data", "science", "data science"] }"""
    deserialized = deserialize_json(serialized)
    assert check_topic_in_json(deserialized, "data science")
    assert not check_topic_in_json(deserialized, "AI")


def test_fetch_github_repos():
    repos = fetch_github_repos("joelgrus")
    assert len(repos) > 0
    assert isinstance(repos[0], dict)


def test_extract_repo_creation_dates():
    repos = fetch_github_repos("joelgrus")
    dates = extract_repo_creation_dates(repos)
    assert len(dates) > 0
    assert dates[0].year >= 2000  # Just a sanity check


def test_count_repos_by_month():
    repos = fetch_github_repos("joelgrus")
    dates = extract_repo_creation_dates(repos)
    month_counts = count_repos_by_month(dates)
    assert isinstance(month_counts, Counter)


def test_count_repos_by_weekday():
    repos = fetch_github_repos("joelgrus")
    dates = extract_repo_creation_dates(repos)
    weekday_counts = count_repos_by_weekday(dates)
    assert isinstance(weekday_counts, Counter)


def test_get_last_5_repo_languages():
    repos = fetch_github_repos("joelgrus")
    languages = get_last_5_repo_languages(repos)
    assert len(languages) == 5
