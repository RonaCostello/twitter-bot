import tweepy
from secrets import *
from panoptes_client import Panoptes, Project
from randomproject import random_project
import sys, pdb, pprint
import requests
import os

def tweet_image(url, message):
    api = twitter_api()
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("could not download image")


def twitter_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth)




if __name__ == '__main__':

    project = random_project()
    avatar = project.avatar
    avatar_url = avatar['media'][0]['src']
    message = "Check out this project"

    tweet_image(avatar_url, message)
