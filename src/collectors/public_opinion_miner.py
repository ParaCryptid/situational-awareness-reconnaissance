import tweepy
from transformers import pipeline

class PublicOpinionMiner:
    def __init__(self, twitter_api_keys):
        """
        Initialize the miner with Twitter API keys and sentiment analysis pipeline.
        :param twitter_api_keys: Dictionary with Twitter API keys (API key, API secret, access token, access token secret).
        """
        auth = tweepy.OAuthHandler(twitter_api_keys['api_key'], twitter_api_keys['api_secret'])
        auth.set_access_token(twitter_api_keys['access_token'], twitter_api_keys['access_token_secret'])
        self.twitter_api = tweepy.API(auth)
        self.sentiment_analyzer = pipeline("sentiment-analysis")

    def collect_tweets(self, keyword, count=100):
        """
        Collect tweets based on a specific keyword.
        :param keyword: The keyword to search for.
        :param count: Number of tweets to collect (default: 100).
        :return: List of tweet texts.
        """
        tweets = self.twitter_api.search(q=keyword, count=count, lang="en", tweet_mode="extended")
        return [tweet.full_text for tweet in tweets]

    def analyze_sentiment(self, tweets):
        """
        Analyze sentiment of a list of tweets.
        :param tweets: List of tweet texts.
        :return: Sentiment analysis results.
        """
        return self.sentiment_analyzer(tweets)

# Example usage
# twitter_keys = {
#     "api_key": "your_api_key",
#     "api_secret": "your_api_secret",
#     "access_token": "your_access_token",
#     "access_token_secret": "your_access_token_secret"
# }
# miner = PublicOpinionMiner(twitter_keys)
# tweets = miner.collect_tweets("example_keyword")
# sentiment = miner.analyze_sentiment(tweets)
# print(sentiment)
