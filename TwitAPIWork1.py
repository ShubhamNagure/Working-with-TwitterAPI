import tweepy

auth = tweepy.OAuthHandler("FnMFgbEqZub5SXRDdx6lgI8fu", "XKDwUzSEcxsE6jt8qqsa4FR0Ufpmg21e6SflPekIscizvFZv71")
auth.set_access_token("832732350-UjPXQW59OkkAQ19K5tZvjFyDk6E9rPrwvDZ4VmMk", "yYxswg5yJH2YJmZg9MVznEynEO3oXCwhgrMQBBjmq2hP7")

api = tweepy.API(auth)
public_tweets = api.home_timeline()


for tweet in public_tweets:
    print(tweet.text)
    print(20*'-------')