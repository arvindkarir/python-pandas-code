# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:22:44 2017
When we insert the first element, the probability of not having a collision is 1. For second insertion, since there are n-1 hash results left that are not equal to the result of the first hash, n-1 out of n choices will not yield a collision. So, the probability of not getting a collision on the second insertion is (n-1)/n and the probability of not getting a collision on either of the first two insertions is 1*[(n-1)/n]*[(n-2)/n]. We can multiply these probabilities because for each insertion the value produced by the hash function is independent of anything that has preceded it. The probability of not having a collision after K insertions is 1*[(n-1)/n]*[(n-2)/n]*...*[({n-(k-1)}/n] """
import random

def collisionProb(n, k): #see explanation above
    prob = 1.0
    for i in range(1, k):
        prob = prob * ((n - i)/float(n))
    print( 1 - prob)

""" if there are p places available and n insertions to be made such that each insertion is a random number generated in the range of 0 to p - defined as choices. used is an array of hashValues stored in pth place. Basically we are detecting for a 0 or 1.
"""    
def simInsertions(placeSlot, numInsertions):
    used = []
    choices = range(placeSlot)
    for i in range(numInsertions):
        hashValue = random.choice(choices)
        if hashValue in used:
            return 1
        else:
            used.append(hashValue)
    return 0
 
"""we are running numTrials and incrementing the collisions by return values from def_simInsertions function. this is divided by the numTrials to give probability
"""               
def findProb(numTrials, placeSlot, numInsertions):
    collisions = 0.0
    for t in range(numTrials):
        collisions += simInsertions(placeSlot, numInsertions)
    return collisions/numTrials 


print('Actual probability of a collision =', collisionProb(1000, 50))
print('Est. probability of a collision =', findProb(1000, 50, 10000))
print('Actual probability of a collision =', collisionProb(1000, 200))
print('Est. probability of a collision =', findProb(1000, 200, 10000))       