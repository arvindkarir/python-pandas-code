# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:56:33 2017

@author: User
"""
import random
   
def toss(n):
    heads, tails = 0, 0 #initialize variables
    outCome = ''
    headTail = [1,2] #possible outcomes of coin toss, heads or tails
    for i in range(n): #no of tosses
        outCome = random.choice(headTail) #choose between head/tail
        if outCome == 1:
            heads += 1
        else:
            tails += 1
    return heads/n

def tossSim(flipsperTrial, numTrials):
    fracHeads = [] #initializing a list
    for i in range(numTrials):
        fracHeads.append(toss(flipsperTrial)) #creating a list of outcomes of each trial
    print(fracHeads)
    mean = sum(fracHeads)/len(fracHeads) #evident after print(fracHeads)
    return mean
    

def tossPlot(minTrials, maxTrials):
    #ratios = []
    #diffs = []
    xaxis = []
    for n in range(minTrials, maxTrials +1):
        xaxis.append(2**n)
    print(xaxis)    
