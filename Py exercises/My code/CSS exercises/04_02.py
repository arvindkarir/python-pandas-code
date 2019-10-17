# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:42:10 2017

@author: User
"""

tweets = ["#1:-@DanClark:-The party was amazing",
          "#19:-@NatalyS:-Avoid 401 Toronto area at this time",
          "#50:-@CBCNews:-How Canadian captain gave her team a speech",
          "#14:-@DanClark:-The food was good",
          "#15:-@DaveLin:-Lucky you DanClark"]

def afn(tweets, lookName):
    names = list(map(lambda x: x.split(':-', 2)[1], tweets)) # splits to a max no of '2' splits and returns [1]st element of split string'
    tweetNos = list(map(lambda x: x.split(':-', 1)[0], tweets)) # applies lambda split function and returns the tweet number
    lookUp = list(filter(lambda n: n.startswith(lookName), names)) # a list of DanClark in the names list
    newList = list(map(lambda x, y: x+y, tweetNos , names))
    lookUpnew = list(filter(lambda n: n.endswith(lookName), newList)) # a list of DanClark in the names list
    justNo = list(map(lambda x: x.split('@', 1)[0], lookUpnew)) #extracting numbers with lookName
    print(names, tweetNos, lookUp, newList, lookUpnew, justNo) # all the values
    list(map(print, justNo)) # a way to print
    print(*justNo, sep = '\n') # another way to print


afn(tweets, "@DanClark")

# Amour's code
#
#def getTweetNumber(tweet):
#  return int(tweet[1: tweet.find(':')])
#
#def bfn(tweets, name):
#  return list(map(getTweetNumber, filter(lambda twt: name in twt, tweets)))


# not working ======
# This only works for next value, not sure how to increment +1 without a for loop or recursive function
#from itertools import cycle
#iterator = cycle(tweets)
#    print(next(iterator))
# some other lines...
#    map((lambda names, tweetNos: names + tweetNos), names)
#    joinList = list(map(print, tweets))
#    brokenList = tweets.split(', ')

# Equivalency:
# tweetNos = [i.split(':-', 1)[0] for i in tweets] # returns the tweet number
# IS SAME AS...
# diffList = list(map(lambda x: x.split(':-', 1)[0], tweets))
# names = [i.split(':-', 2)[1] for i in tweets] # splits to a max no of '2' splits and returns [1]st element of split string'