import random
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler

consumer_key = 'remove'
consumer_secret = 'remove'
access_token = 'remove'
access_token_secret = 'remove'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
def genTweet():
    tweets = open('C:/Users/Will/PycharmProjects/filepractice/tweets.txt', 'r')
    nums = []
    rando = random.randint(0, 2538)
    while rando in nums:
        rando = random.randint(0, 2538)
    nums.append(rando)
    i = 1
    for line in tweets:
        if i == rando:
            break
        i += 1
    tweet = line
    print(rando)
    print(tweet)
    tweets.close()
    return tweet
def sendTweet():
    api.update_status(status = genTweet())
sendTweet()
scheduler = BlockingScheduler()
scheduler.add_job(sendTweet, 'interval', minutes = 15)
scheduler.start()
