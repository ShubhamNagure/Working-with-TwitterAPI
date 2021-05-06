import tweepy

auth = tweepy.OAuthHandler("--some key----", "---some more key----------")
auth.set_access_token("----some token-------------", "------------some more token---")

api = tweepy.API(auth)
public_tweets = api.home_timeline()


for tweet in public_tweets:
    print(tweet.text)
    print(20*'-------')
