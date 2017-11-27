
import tweepy
import time #https://github.com/tweepy/tweepy

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "eEmuwSsPY2EYMo2YgPxE1gZ8f"
consumer_secret = "2SoByjLZoJis8ZWFvPkeM1ATBFWeUCZ4JfHQIoFKz9VKO7xnEp"
access_key = "994594207-1BiNej6Ut0mV1NIuYGHchs0cDg6fIMc7VkN9qGqA"
access_secret = "44atRtNKV0VnnXKH1boOr2EYIC9HGtlbOTt5hyh8stUtM"

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile

# uses the function to query a Twitter user. Try s = get_profile("cd_conrad")
s = get_profile("CitronResearch")
print "Name: "+s.name
print "Location: "+s.location
print "Description: "+s.description
print "Id: "+s.id_str