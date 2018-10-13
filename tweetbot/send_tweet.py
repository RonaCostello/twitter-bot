import tweepy
from secrets import *
from panoptes_client import Panoptes, Project
from randomproject import random_project
import sys, pdb, pprint
import requests
import os
import random


def fetch_random_project_max_len_280(message):
    project = random_project()
    if length_of_tweet(project, message) > 280:
        fetch_random_project_max_len_280(message)
    return project

def length_of_tweet(project, message):
    twitter_url_chars = 23
    project_name_chars = len(project.title)
    project_description_chars = len(project.description)
    tweet_length = twitter_url_chars + project_name_chars + project_description_chars + message
    return tweet_length

def twitter_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth)

def get_avatar_url(project):
    avatar = project.avatar
    avatar_url = avatar['media'][0]['src']
    return avatar_url

def tweet_image(project, message):
    image_url = get_avatar_url(project)
    api = twitter_api()
    filename = 'temp.jpg'
    request = requests.get(image_url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("could not download image")

def tweet_no_image(message):
    api = twitter_api()
    api.update_status(status = message)



if __name__ == '__main__':
    project = fetch_random_project_max_len_280(1)

    message_pt1 = "Check out the project "
    message_pt2 = " on the Zooniverse: "
    message_len = len(message_pt1 + message_pt2)

    project = fetch_random_project_max_len_280(message_len)

    print(project.title)

    simple_tweet = message_pt1 + project.title + message_pt2
    descriptive_tweet = simple_tweet + project.description

    # randomly tweet with a message or not
    tweet = random.choice([simple_tweet, descriptive_tweet]) + " https://www.zooniverse.org/projects/" + project.slug

    tweet_image(project, tweet)
    # tweet_no_image(tweet)
