# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:43:28 2018

@author: User
"""

def splitLines(S):
    mylist = []
    counts = {}
    for lines in S:
        lines = str(lines.replace('.','').replace(',',''))
        mylist += [lines]
    wordfreq = []
    for line in mylist:
        somelist = []
        for i in line.split():
#            print(i)
            wordfreq.append(line.count(i))
    somelist += mylist, wordfreq
    print(somelist)
#    print(wordlist)
    printOut(counts, mylist)


def printOut(counts, mylist):
    wordlist = listofwords(mylist)
    counts = (countword(wordlist))
    for key, vals in counts.items():
        print('[%s] => [%s]' % ( str(key), str(vals)))

def listofwords(astring):
    wordlist = []
    for element in astring:
        word = element.split()
        wordlist += word
    return wordlist

def countword(somewords):
    counts = dict()
    for word in somewords:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    return counts


S = ['CS116 is difficult.', 'However, is CS116 is also full of fun.']
#somefn(S)
(splitLines(S))