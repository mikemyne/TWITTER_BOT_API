

import tweepy
import time

# Copying the API key and API secret key THEN the Token
# Copying the Access token and Access token secret
auth = tweepy.OAuthHandler('QHogJEpfVODRXXc2IQV5BUyxq','n0M2NEiItMAUdFtwVDh5Y3VHaMr3cr7bGkwAPLH5TjY5BdKRAT')
auth.set_access_token('981379777209749504-nAxITLbO8ffOPmJNnGe2K2A1v8q7mSK','mVbAiO80BAeTQ38D34ZcIMYZphs6oKu2nEkhrQZJ1gkdy')


# The "auth" authenticates us
# The "wait on rate limit" will pause once we reach a like limit
# The "wait on rate limit notify" will notify
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Fetching my details
user = api.me()


# The "tweepy.Cursor" scrolls through all the content which in this case is followers
# It will print the name of all the people who follow you

#for follower in tweepy.Cursor(api.followers).items():
    #print(follower.name)

# Code if you want to follow someone back that already follows you

#for follower in tweepy.Cursor(api.followers).items():
    #if follower.name == "James Smith":
         #follower.follow()


# In the "search" input what you want to search about
# Also input the number of tweets you want from that search
search = 'marvel'
numberOfTweets = 500


for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        print("Tweets Liked by Myne")
        tweet.favorite()
        time.sleep(10)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

