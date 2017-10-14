from twitterclient import get_twitter_client
import json
username=input("Enter username to retrieve follower list ")
client = get_twitter_client()
profile = client.get_user(screen_name=username)
print(json.dumps(profile._json, indent=4))