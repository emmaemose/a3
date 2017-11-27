#Twitter Profiler app. This is a simple script to configure the Twitter API

import tweepy
import time #https://github.com/tweepy/tweepy
import csv

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview

consumer_key = "eEmuwSsPY2EYMo2YgPxE1gZ8f"
consumer_secret = "2SoByjLZoJis8ZWFvPkeM1ATBFWeUCZ4JfHQIoFKz9VKO7xnEp"
access_key = "994594207-1BiNej6Ut0mV1NIuYGHchs0cDg6fIMc7VkN9qGqA"
access_secret = "44atRtNKV0VnnXKH1boOr2EYIC9HGtlbOTt5hyh8stUtM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile

#this function collects twitter profile tweets and returns Tweet objects
def get_tweets(screen_name):
    try:
        #https://developer.twitter.com/en/docs/tweets/timelines/overview describes user_timeline
        tweets = api.user_timeline(screen_name, count=20)
    except:
        user_profile = "broken"
    return tweets

# uses the function to query a Twitter user. Try s = get_profile("km664737")
list1= []
t = get_tweets("CitronResearch")
for tweet in t:
    list1.append(tweet.retweet_count)
for tweet in t:
    if tweet.retweet_count == max(list1):
        text = tweet.text

with open ('tweets.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    for tweet in t:
        if "FTC" in tweet.text:
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
    t2 = get_tweets("Shopify")
    for tweet in t2:
        if "citron" in tweet.text:
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
print "most popular tweet of citron research is: \"" + text + " \" with a retweet count of " +str(max(list1))