# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:29:15 2017
Generates 6^n sequences of SIX consequetive die rolls
@author: User
"""
import random
def rollone():
    outCome = ''
    someRange = [1,2,3,4,5,6] #possible outcomes of roll
    for i in range(n):
        outCome = outCome + str(random.choice(someRange)) #pick a number from range
    return outCome

def rollN(n):
    result = '' #initialize string
    for j in range(6**n): # no of rolls of die
        result = result + str(rollone()) + ' ' # make a string
    print(result)