from twitterclient import get_twitter_client
import json

s = (input("Enter name to get JSON based  info :"))
client = get_twitter_client()
profile = client.get_user(screen_name=s)
print(json.dumps(profile._json, indent=4))