# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:19:25 2018

@author: User
"""
def searchtweets(s, nameof):
    tweetnos = []
    for each in s:
        eachtweet = (each.split(':-'))
        if nameof in eachtweet:
            print(eachtweet[0], eachtweet[1].strip('@'))
            tweetnos.append(int(eachtweet[0].strip('#')))
    print(tweetnos)


tweets = [
 '#1:-@DanClark:-The party was amazing',
'#19:-@NatalyS:-Avoid 401 Toronto area at this time',
'#50:-@CBCNews:-How Canadian captain gave her team a speech',
'#14:-@DanClark:-The food was good',
'#15:-@DaveLin:-Lucky you DanClark'
]
searchtweets(tweets, "@DanClark")