# Chap02-03/twitter_client.py
import os
import sys
from tweepy import API
from tweepy import OAuthHandler


def get_twitter_auth():
    try:
        consumer_key = "9p75Tc0vO5JikeBbFfrj6YSRO"
        consumer_secret = "fP70eIVZ0u9zzprN5ZKHtbor9K3zD3YO6Gmpff7ZDf9XEfj8XA"
        access_token = "3528595993-aaODwuEXLFdwAFaFGuaCYd0vI6qu2yJbIVGbMta"
        access_secret = "2P2UJMNbbSTvwcKdmKloHrqwCcCN23D5cEIAWu4hUM9YE"






    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth


def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client
