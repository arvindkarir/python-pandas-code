# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:42:48 2018

@author: User
"""

#def getNames():
#    nameFile = open('names.txt', 'r')
#    readFile = nameFile.readlines()
#    Types = [line.split("\n") for line in readFile]
#    print(Types)
#    nameList = [Type[0] for Type in Types]
#    print(nameList)
#    listOfNames = []
#    for aName in nameList:
#        listOfNames.append(aName.split( ' '))
#    return listOfNames
#
#print(getNames())


def aDictMethod(dict1):
    revDict = {}
    for k, v in dict1.items():
        if v not in revDict:
            revDict[v] = set()
        revDict[v].add(k)
    return revDict

dict1 = {'Europa': 'Jupiter', 'Psamathe': 'Neptune', 'Cordelia': 'Uranus', 'Cupid': 'Uranus'}

print(aDictMethod(dict1))
