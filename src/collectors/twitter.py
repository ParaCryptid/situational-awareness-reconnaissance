
import tweepy

def collect_tweets(api_key, api_secret, access_token, access_token_secret, query, count=100):
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.search_tweets(q=query, count=count, lang="en", tweet_mode="extended")
    return [{"text": tweet.full_text, "user": tweet.user.screen_name} for tweet in tweets]
