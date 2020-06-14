#from credentials import *
from os import environ
import datetime
from time import sleep
import tweepy
import rnn_naruto
import sys


INTERVAL = 60 * 60 * 6  # tweet every 6 hours

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
auth = tweepy.OAuthHandler(environ['CONSUMER_KEY'],
                           environ['CONSUMER_SECRET'])
auth.set_access_token(environ['ACCESS_TOKEN'],
                      environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

model = rnn_naruto.fit_model()  # rnn


def generate_name_for_tweet():
    names = rnn_naruto.get_names(model)
    return names


def tweets():
    names = generate_name_for_tweet()
    for i in range(4):
        try:
            print('new tweet')
            api.update_status('Generated name of the RNN: '+names[i])
            sleep(30)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


def search_tweet_print():
    for tweet in tweepy.Cursor(api.search, q='#naruto').items(10):
        print('Tweet by: @' + tweet.user.screen_name)


def search_tweet_retweet():
    for tweet in tweepy.Cursor(api.search, q='#naruto').items(4):
        try:
            print('new retweet')
            tweet.retweet()
            sleep(30)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


def bot_run():
    print('bot running')
    while True:
        tweets()
        search_tweet_retweet()
        sleep(60)


bot_run()
