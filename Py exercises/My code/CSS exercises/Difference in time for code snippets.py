# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:00:40 2017

@author: User
"""

import time
L = [1,2,3,4,5,6,7,8,9,11,2,12,1,3]

def testTime():
    start = int(round(time.time()*1000))
    for i in range(100000):
        aFn(L)
    end = int(round(time.time()*1000))
    print(end - start)

def aFn(L):
    diff = 0
    for x in L:
        diff += abs(x - sum(L)/len(L))

def aFn2(L):
    diff = 0
    mean = sum(L)/len(L)
    for x in L:
        diff += abs(x-mean)

testTime()