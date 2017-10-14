# Chap02-03/twitter_get_user_timeline.py
import sys
import json
from tweepy import Cursor
from twitterclient import get_twitter_client

def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    user = "sanjiva"
    client = get_twitter_client()

    # fo = open("foo.txt", "w")
    # fo.write("Python is a great language.\nYeah its great!!\n");

    fname = "timeline{}.jsonl".format(user)
    with open(fname, 'w') as f:
        for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16):
            for status in page:
                f.write(json.dumps(status._json) + "\n")
            # print((status["text"].encode("ascii", "ignore") + "\n"))
            # print("(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore")))
                #

