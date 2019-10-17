# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:43:28 2018

@author: User
"""

def splitLines(S):
    mylist = []
    for lines in S:
        lines = str(lines.replace('.','').replace(',',''))
        mylist += [lines]
#    print(mylist)
    wordfreq = []
    for line in mylist:
        somelist = []
        for i in line.split():
            print(i)
            wordfreq.append(line.count(i))
        somelist += mylist, wordfreq
    print(somelist)
#    wordlist = listofwords(mylist)
##    print(wordlist)
#    counts = (countword(wordlist))
#    for word  in list((wordlist)):
#        for key, value in counts.items():
#            if key == word:
#                print([key, value])


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



# some additional code:
#def countword(S):
#    finalLines = ''
#    for lines in S:
#        lines = str(lines.replace('.','').replace(',',''))
#        positionof = enumFn(lines)
#        finalLines += lines + ' '
#        allwords = str.split(lines)
#        print(allwords, positionof)
#
#
#def enumFn(lines):
#    newlist = []
#    for item, index in (enumerate(lines.split())):
#        newlist = newlist + [item]
#    return newlist
#
#
#document1 = ['CS116 is difficult.', 'However, CS116 is also full of fun.']
#(countword(document1))
######################################
# another one
#def stripfn(S):
#    for lines in (S):
#        lines = str(lines.replace('.','').replace(',',''))
#        for i in enumerate(lines.split()):
#            print(i)
#    for i in range(len(S)):
#        mylist = S[i]
#        print(countword(mylist))
#
#def countword(astring):
#    counts = dict()
#    allwords = str.split(astring)
#    for word in allwords:
#        if word in counts:
#            counts[word] +=1
#        else:
#            counts[word] = 1
#    return counts
#
#def count_consecutive(string, start_pos):
#    index = start_pos
#    while (index < len(string) and string[start_pos] == string[index]):
#        index += 1
#    return index - start_pos
#
#
#document1 = ['CS116 is difficult.', 'However, also CS116 is also full of fun.']
#(stripfn(document1))