import tweepy
from secrets import *
from panoptes_client import Panoptes, Project
from randomproject import random_project
import sys, pdb, pprint
import requests
import os


def twitter_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    print tweepy.API(auth)






if __name__ == '__main__':
    twitter_api()
