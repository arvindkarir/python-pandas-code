# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:29:15 2017
Generates 6^n sequences of 'n' consequetive die rolls
@author: User
"""
import random
global n
   
def rollN(n):
    result = '' #initialize string
    outCome = ''
    someRange = [1,2,3,4,5,6] #possible outcomes of roll
    for j in range(6**n): # no of possible sequences of n rolls
        for i in range(n):
            outCome = outCome + str(random.choice(someRange)) + ',' #pick a number from range
    result = result + str(outCome) # makes a string
    print(result)
    
    