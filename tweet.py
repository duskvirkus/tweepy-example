
import tweepy 
from random import *
from time import sleep 
from credentials import * 
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet = 'Hello world! ' + str(random())
  
api.update_status(tweet)
