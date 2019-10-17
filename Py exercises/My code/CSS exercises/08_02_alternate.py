# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:57:41 2018

@author: User
"""

def abbreviate(s):
    alphaset = []
    newstring = ''
    for i in range(ord('a'), ord('z')+1):
        alphaset.append(chr(i))
    for i in range(len(s)):
        count = 1
        if s[i-1] == s[i]:
            count += 1
            print(s[i],count)
            newstring += (str(count))
        else:
            newstring += (s[i])
    print(newstring)


s = 'coffee'
abbreviate(s)