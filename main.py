import random
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler
#start loop, generate a rando, check if it's been genned before with the array, if not, grab that line and
#store it in a string, put the genned rando into an array of ints, end loop

consumer_key = '9Eu3kdMGHtVDes6eM1M3Q9Tt8'
consumer_secret = 'CQPomif23wmehGZCSw5C3PG5NfjUQRz3FqtavEM6xpL8BuwUpw'
access_token = '1095060565075079168-Kld1F0GG2PpTH8CsxBkESm0heSPTbB'
access_token_secret = '7TAsvnO39vYgMUDNFh7mG7TsLqctxBegJBCdGVgMKA2JB'
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
