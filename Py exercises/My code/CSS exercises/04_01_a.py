# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 13:30:12 2017

@author: User
"""

def createOdds(n):
    if n%2 == 0:
        topNo = n-1
    else:
        topNo = n -2
    genOdd(topNo)

def genOdd(topNo):
    print(topNo)
    if topNo == 1:
        return
    else:
        return genOdd(topNo - 2)

createOdds(17)