# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:25:40 2018

@author: User
"""

def abbrS(S):
    characters = {}
    newList = []
    for letter in S:
        if letter not in characters.keys():
            characters[letter] = 1
        else:
            characters[letter] +=1
    print(characters)
    for k in characters:
        if characters[k] == 1:
            newList = newList + [k]
        else:
            newList = newList + [k]
            newList.append(str(characters[k]))
    newnewList = ''.join(newList)
    return newnewList

print(abbrS('coffee'))