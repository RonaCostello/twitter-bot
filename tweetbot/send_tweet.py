import tweepy
from secrets import *
from panoptes_client import Panoptes, Project
from randomproject import random_project
import sys, pdb, pprint
import requests
import os

def tweet_no_image(message):
    api = twitter_api()
    api.update_status(status = message)


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
    print "intro:"
    print project.introduction
    avatar = project.avatar
    avatar_url = avatar['media'][0]['src']
    simple_message = "Check out " + project.title + " on the Zooniverse " + "https://www.zooniverse.org/projects/" + project.slug
    descriptive_message = "Check out " + project.title + " on the Zooniverse - " + project.description + " https://www.zooniverse.org/projects/" + project.slug

    tweet_image(avatar_url, descriptive_message)
    tweet_no_image(descriptive_message)


# # pp.pprint(project.__dict__)
