# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:56:33 2017

@author: User
"""
import random
import pylab

def tossPlot(minTrials, maxTrials):
    ratios, diffs, xaxis = [], [], []
    #diffs = []
    #xaxis = []
    for n in range(minTrials, maxTrials +1):
        xaxis.append(2**n)
    #print(xaxis) #the number of times coin is tossed
    for numFlips in xaxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        #print(numHeads, numTails)
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    #print(ratios, diffs)
    pylab.title('Difference between Heads and Tails')
    pylab.semilogx('Number of tosses')
    pylab.ylabel('abs(#ofHeads - #ofTails)')
    pylab.plot(xaxis, diffs, 'bo')
    pylab.figure()
    pylab.title('Heads/Tails ratios')
    pylab.semilogx('Number of tosses')
    pylab.ylabel('#ofHeads/#ofTails')
    pylab.plot(xaxis, ratios, 'bo')
#random.seed(0) #used to generate the same 'random' sequence every time, useful for debugging
tossPlot(4, 20)
