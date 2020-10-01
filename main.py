from textblob import TextBlob
from config import *
from utils import *
import tweepy
import time


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)


def reply():
    tweets = api.mentions_timeline(read_last_id(file_name), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#hackwithdscmait' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text + ' replied')
            blob = TextBlob(tweet.full_text)
            if blob.sentiment.polarity > 0:
                # api.update_status('@' + tweet.user.screen_name + " Thanks for attending our session! Follow us to get updates about latest events", tweet.id)
                api.create_favorite(tweet.id)
                api.retweet(tweet.id)
                store_last_id(file_name, tweet.id)

            else:
                print(str(tweet.id) + ' - ' + tweet.full_text + ' rejected')
                try:
                    api.send_direct_message(tweet.user.id, "We are sorry you didn't had a great time! Can you give us some feedback or suggestions?") 
                except:
                    pass
                store_last_id(file_name, tweet.id)

        else:
            pass
                
while True:
    reply()
    time.sleep(300)