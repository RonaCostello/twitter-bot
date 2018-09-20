import unittest
import tweepy
from tweetbot import send_tweet

class TestTweetbotFunction(unittest.TestCase):

    def setUp(self):
        self.api = send_tweet.twitter_api()

    def test_API(self, msg = 'twitter_api returns an instance of a tweepy api'):
        self.assertIsInstance( self.api, tweepy.API )
