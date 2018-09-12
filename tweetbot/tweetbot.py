import tweepy
from secrets import *
from randomproject import random_project

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

project = random_project()

def simple_tweet():
    tweet = "Check out " + project.title + " on the Zooniverse " + "https://www.zooniverse.org/projects/" + project.slug
    api.update_status(status = tweet)


def descriptive_tweet():
    tweet = "Check out " + project.title + " on the Zooniverse, " + project.description + " https://www.zooniverse.org/projects/" + project.slug
    api.update_status(status = tweet)

simple_tweet()

descriptive_tweet()
