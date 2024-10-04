# Test functions
from twython import Twython

from data_scrape_from_scratch.c09_getting_data.e0908_twitter import (
    get_top_hashtags,
    search_tweets,
    get_twitter_client,
    get_temp_client,
    CONSUMER_KEY,
    CONSUMER_SECRET, get_final_tokens, get_authentication_url, authorize_application
)


def test_get_temp_client():
    client = get_temp_client(CONSUMER_KEY, CONSUMER_SECRET)
    assert isinstance(client, Twython)


def test_search_tweets():
    client = get_temp_client(CONSUMER_KEY, CONSUMER_SECRET)
    temp_creds = get_authentication_url(client)
    pin_code = authorize_application(temp_creds['auth_url'])
    final_step = get_final_tokens(client, temp_creds,pin_code)
    ACCESS_TOKEN = final_step['oauth_token']
    ACCESS_TOKEN_SECRET = final_step['oauth_token_secret']
    twitter = get_twitter_client(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    tweets = search_tweets(twitter, "data science")
    assert len(tweets) > 0
    assert isinstance(tweets[0], dict)


def test_get_top_hashtags():
    sample_tweets = [
        {"entities": {"hashtags": [{"text": "data"}, {"text": "science"}]}},
        {"entities": {"hashtags": [{"text": "science"}, {"text": "AI"}]}},
    ]
    top_hashtags = get_top_hashtags(sample_tweets)
    assert top_hashtags == [('science', 2), ('data', 1), ('ai', 1)]
