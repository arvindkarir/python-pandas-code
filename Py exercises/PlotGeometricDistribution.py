# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:07:40 2017

@author: User
"""
import pylab
import random

def successfulStarts(eventProb, numTrials):
    """Assumes eventProb is a float representing a probability
    of a single attempt being successful. numTrials a positive int
    Returns a list of the number of attempts needed before a
    success for each trial."""
    triesBeforeSuccess = []
    for t in range(numTrials):
        consecFailures = 0
        while random.random() > eventProb:
            consecFailures += 1
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

random.seed(0)
probOfSuccess = 0.5
numTrials = 5000
distribution = successfulStarts(probOfSuccess, numTrials)
pylab.hist(distribution, bins = 14)
pylab.xlabel('Tries Before Success')
pylab.ylabel('Number of Occurrences Out of ' + str(numTrials))
pylab.title('Probability of Starting Each Try ' + str(probOfSuccess))
    
