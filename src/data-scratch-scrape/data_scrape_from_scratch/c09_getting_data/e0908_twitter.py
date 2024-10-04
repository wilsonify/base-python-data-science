import os
import webbrowser
from collections import Counter
from typing import List, Dict
from twython import Twython, TwythonStreamer

CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")

# Twitter Authentication
def get_temp_client(consumer_key: str, consumer_secret: str) -> Twython:
    """Get a temporary Twython client for authentication."""
    return Twython(consumer_key, consumer_secret)


def get_authentication_url(client: Twython) -> Dict:
    """Get authentication tokens and return the authorization URL."""
    return client.get_authentication_tokens()


def authorize_application(url: str) -> str:
    """Prompt the user to visit the URL and get the PIN code for authorization."""
    print(f"go visit {url} and get the PIN code and paste it below")
    webbrowser.open(url)
    pin_code = input("please enter the PIN code: ")
    return pin_code


def get_final_tokens(client: Twython, temp_creds: Dict, pin_code: str) -> Dict:
    """Exchange the PIN code for the final OAuth tokens."""
    auth_client = Twython(CONSUMER_KEY,
                          CONSUMER_SECRET,
                          temp_creds['oauth_token'],
                          temp_creds['oauth_token_secret'])
    return auth_client.get_authorized_tokens(pin_code)


def get_twitter_client(consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str) -> Twython:
    """Return an authenticated Twython instance."""
    return Twython(consumer_key, consumer_secret, access_token, access_token_secret)


# Search Tweets
def search_tweets(twitter: Twython, query: str) -> List[Dict]:
    """Search for tweets containing a specific query."""
    return twitter.search(q=query)["statuses"]


def print_tweets(tweets: List[Dict]):
    """Print out users and tweets."""
    for status in tweets:
        user = status["user"]["screen_name"]
        text = status["text"]
        print(f"{user}: {text}\n")


# Stream Tweets
class MyStreamer(TwythonStreamer):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, tweet_limit=100):
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)
        self.tweets = []
        self.tweet_limit = tweet_limit

    def on_success(self, data):
        """Handle successful data reception (tweets)."""
        if data.get('lang') == 'en':  # Only collect English tweets
            self.tweets.append(data)
            print(f"received tweet #{len(self.tweets)}")
        if len(self.tweets) >= self.tweet_limit:
            self.disconnect()

    def on_error(self, status_code, data):
        """Handle error responses from Twitter."""
        print(status_code, data)
        self.disconnect()

    def get_tweets(self) -> List[Dict]:
        """Return the list of collected tweets."""
        return self.tweets


# Collecting Hashtags
def get_top_hashtags(tweets: List[Dict], n: int = 5) -> List:
    """Find the most common hashtags in the collected tweets."""
    hashtags = Counter(
        hashtag['text'].lower()
        for tweet in tweets
        for hashtag in tweet["entities"]["hashtags"]
    )
    return hashtags.most_common(n)



if __name__ == "__main__":
    # Run authentication process
    temp_client = get_temp_client(CONSUMER_KEY, CONSUMER_SECRET)
    temp_creds = get_authentication_url(temp_client)
    pin_code = authorize_application(temp_creds['auth_url'])
    final_tokens = get_final_tokens(temp_client, temp_creds, pin_code)

    # Get authenticated twitter client
    twitter = get_twitter_client(CONSUMER_KEY, CONSUMER_SECRET, final_tokens['oauth_token'],
                                 final_tokens['oauth_token_secret'])

    # Search for tweets
    tweets = search_tweets(twitter, '"data science"')
    print_tweets(tweets)

    # Stream tweets (collect up to 100 tweets containing "data")
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, final_tokens['oauth_token'], final_tokens['oauth_token_secret'])
    stream.statuses.filter(track='data')
    collected_tweets = stream.get_tweets()

    # Find the top 5 hashtags
    top_hashtags = get_top_hashtags(collected_tweets, 5)
    print(f"Top hashtags: {top_hashtags}")

