import unittest
import tweepy
from tweetbot import send_tweet
from tweetbot import randomproject


class TestTweetbotFunction(unittest.TestCase):

    def setUp(self):
        self.api = send_tweet.twitter_api()
        self.title = "x" * 50
        self.description = "x" * 50
        self.message = "x" * 50

    def test_api(self, msg = 'twitter_api returns an instance of a tweepy api'):
        self.assertIsInstance( self.api, tweepy.API )

    def test_length_of_tweet(self):
        project_url = "x" * 23
        tweet_length = len(self.title + self.description + self.message + project_url)
        self.assertEqual( send_tweet.length_of_tweet(self),  tweet_length )
