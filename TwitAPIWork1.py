import tweepy

auth = tweepy.OAuthHandler("FnMSfFgbEqZghDgGhjub5SXabRDdx6lgI8fu", "XKDwUzSEhgftYsjkAnkQcxsE6jt8qqsgfvhja4FR0Ufpmg21e6SfhfallPekIscizvFZv71")
auth.set_access_token("832732350-UjPhjkkakljXQW59dfryAwkOkkAQ19K5tZvjFynvgjkagGjGjNkaklHavkDk6E9rPrwvDZ4VmMk", "yYxswg5yJH2YJmZg9ghkfawQxzhMVz67dgjklnEynEO3oXCwhgrMQBBjmq2hP7")

api = tweepy.API(auth)
public_tweets = api.home_timeline()


for tweet in public_tweets:
    print(tweet.text)
    print(20*'-------')
