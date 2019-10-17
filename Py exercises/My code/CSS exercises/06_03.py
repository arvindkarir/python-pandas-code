# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 13:52:01 2017

@author: User
"""
import re

aPara = "this is a list of words. and here is another"
aList = []
print(aPara.split()) # splits into words
print(len(aPara.split())) # count of words

for item in re.split('[.]', aPara): #splits into sentences
    print(item)
    aList.append((len(item.split())))
    print(aList)

print(re.split('[.]', aPara))
print(len(re.split('[.]', aPara))) # number of sentences