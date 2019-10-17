# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 18:18:02 2018

@author: User
"""

def splitLines(S):
    finalLines = ''
    for lines in S:
        lines = str(lines.replace('.','').replace(',',''))
        positionofwords = enumFn(lines)
        finalLines += lines + ' '
        almostlist =  (countword(finalLines))
        print(list(zip(positionofwords, almostlist )))


def countword(astring):
    counts = dict()
    allwords = str.split(astring)
    print(allwords)
    for word in allwords:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
#    return list(zip( (counts.keys()) , (counts.values()))) #    return counts.items()

def enumFn(lines):
    newlist = []
    for item, index in (enumerate(lines.split())):
        newlist = newlist + [item]
    return newlist


S = ['CS116 is difficult.', 'However, CS116 is also full of fun.']

(splitLines(S))

