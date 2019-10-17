# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:05:59 2018

@author: User
"""
#def makeFile():
#    file = open('testfile.txt','w')
#    file.write('hello world\n')
#    file.write('this is a new file\n')
#    file.write('and this is another line\n')
#    file.write('and yet another\n')
#    file.close()
#
#makeFile()

class Name:
    def __init__(self, fn, ln):
        self.first = fn
        self.last = ln

def strNames(L):
    nameslist = L.split()
    return Name(nameslist[0], (nameslist[1]))

def readFile():
    names = open('names.txt','r')
    nextStr = names.readline()
    people = []
    while (nextStr != ""):
        nextName = strNames(nextStr)
        people.append(nextName)
        nextStr = names.readline()
    return list(people)

print(readFile())


