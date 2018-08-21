import tweepy
from secrets import *
from randomproject import select_project

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

print select_project()
