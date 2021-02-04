from django.test import TestCase
from .models import Tweet
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User=get_user_model()

class TweetTestCase(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='abc',password='password1')
        Tweet.objects.create(content='my first tweet',user=self.user)
        Tweet.objects.create(content='my first tweet',user=self.user)
        Tweet.objects.create(content='my first tweet',user=self.user)
        Tweet.objects.create(content='my first tweet',user=self.user)

    def test_tweet_created(self):
        tweet=Tweet.objects.create(content='my second tweet',user=self.user)
        self.assertEqual(tweet.id,2)
        self.assertEqual(tweet.user,self.user)
    
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='password1')
        return client

    def test_tweet_list(self):
        client = self.get_client()
        response=client.get('/api/tweets/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.json()),1)