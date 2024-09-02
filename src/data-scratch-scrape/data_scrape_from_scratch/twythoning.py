from twython import Twython
from twython import TwythonStreamer


class MyStreamer(TwythonStreamer):
    """
    our own subclass of TwythonStreamer that specifies
    how to interact with the stream
    """

    def __init__(self):
        super.__init__()
        self.tweets = []

    def on_success(self, data):
        """what do we do when twitter sends us data?
        here data will be a Python object representing a tweet"""

        # only want to collect English-language tweets
        if data["lang"] == "en":
            self.tweets.append(data)

        # stop when we've collected enough
        if len(self.tweets) >= 1000:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


def call_twitter_search_api():
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)
    # search for tweets containing the phrase "data science"
    for status in twitter.search(q='"data science"')["statuses"]:
        user = status["user"]["screen_name"].encode("utf-8")
        text = status["text"].encode("utf-8")
        print(user, ":", text)
        print()


def call_twitter_streaming_api():
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""
    stream = MyStreamer(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET
    )

    # starts consuming public statuses that contain the keyword 'data'
    stream.statuses.filter(track="data")
