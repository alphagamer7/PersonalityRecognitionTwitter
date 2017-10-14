# demo polarity measures pos an dneg subjectivity measures how opinion and factual
import json
import jsonlines
import sys
from textblob import TextBlob
import os

data = []
tweet=[]
# user
with jsonlines.open('timelinesanjiva.jsonl') as reader:
    for obj in reader:
        # stweet=obj['text'],' ',obj['user']['screen_name']
        stweet = str(obj['text'])
        # print(obj)
        print(stweet)
        # print(stweet)
        analysis=TextBlob(stweet)
        print(analysis.sentiment)
        # tweet.append(stweet)


# print(stweet)
print(tweet)

# l1=[1,3,5,7]
# print(l1)

# print(os.getcwd())
# print(data)

# for item in data:
#     for data_item in item['text']:
#         print (data_item ,end='', flush=True)

# fo = open("foo.txt", "w")
# fo.write( "Python is a great language.\nYeah its great!!\n");