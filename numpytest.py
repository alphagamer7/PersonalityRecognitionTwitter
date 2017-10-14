# import nltk
# # from nltk.book import *
# from nltk.corpus import treebank
# text111=treebank.parsed_sents('wsj_0001.mrg')[0]
# print(text111)
# string1="  dasd      asd sad sa   "
# print(string1.upper())
# s=string1.lstrip()
# print(s)
# #
# # text15 = nltk.word_tokenize("Alice loves Bob")
# # grammar = nltk.CFG.fromstring("""
# # S -> NP VP
# # VP -> V NP
# # NP -> 'Alice' | 'Bob'
# # V -> 'loves'
# # """)
# #
# # parser = nltk.ChartParser(grammar)
# # trees = parser.parse_all(text15)
# # for tree in trees:
# #     print(tree)
#
# # text11="Children shouldn't drink a sugary drink before bed!"
# # print(nltk.word_tokenize(text11))
# #
# # print(text7)
# # # print(list(set(text7))[:5])
# #
# # dist=FreqDist(text7)
# # print(dist)
# # vocal1=dist.keys()
# # print(vocal1)
# # print(dist['million'])
# #
# # freqword=[w for w in vocal1 if len(w) > 5 and dist[w]>100]
# # print(freqword)
# # # udhr = nltk.corpus.udhr.words('English-Latin1')
# # udhr=nltk.corpus.udhr.words('English-Latin1')
# # print(udhr[:5])
#
# # text33="This is the first sentence. Are you high! Sup motherfuycker?? I am feeling so high"
# # sentences=nltk.tokenize.sent_tokenize(text33)
# # print(len(sentences))
# # print(sentences)
# # nltk.help.upenn_tagset('MD')
import datetime

now = datetime.datetime.now()
s = (input("Enter your DOB :"))
s=int(s)
age=now.year-s
print('Your age is ',age)


