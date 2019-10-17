# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:56:43 2017
Important to note that stdDev is defined in code, not imported
@author: User
"""
import random
import pylab

def stdDev(X):
    """Assumes that X is a list of numbers.
        Returns the standard deviation of X"""
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5 #Square root of mean difference

def CV(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

def makePlot(xVals, yVals, title, xLabel, yLabel, style, logX = False, logY = False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()


def runTrials(numFlips):
    numHeads, numTails = 0.0, 0.0
    for n in range(numFlips):
        if random.random() < 0.5:
            numHeads += 1
    numTails = numFlips - numHeads
    return(numHeads, numTails)
    
def flipPlot(minFlips, maxFlips, numTrials):
    ratioMeans, diffMeans = [],[]
    ratioSD, diffSD = [], []
    ratiosCVs, diffsCVs = [], []
    xaxis = []
    for exp in range(minFlips+1, maxFlips +1):
        xaxis.append(2**exp)
    for numFlips in xaxis:
        ratios, diffs = [],[]
        for t in range(numTrials):
            numHeads, numTails = runTrials(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))
        ratioMeans.append(sum(ratios)/float(numTrials))
        diffMeans.append(sum(diffs)/float(numTrials))
        ratioSD.append(stdDev(ratios))
        diffSD.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
    numTrialsString = ' (' + str(numTrials) + ' Trials)' #this is a string used in title for number of trials
    title = 'Mean Heads/Tails Ratios' + numTrialsString
    makePlot(xaxis, ratioMeans, title, 'Number of flips', 'Mean Heads/Tails', 'bo', logX = True)
    title = 'SD Heads/Tails Ratios' + numTrialsString
    makePlot(xaxis, ratioSD, title,'Number of Flips', 'Standard Deviation', 'bo', logX = True, logY = True)

    title = 'Mean abs(#Heads - #Tails)' + numTrialsString
    makePlot(xaxis, diffMeans, title, 'Number of Flips', 'Mean abs(#Heads - #Tails)', 'bo', logX = True, logY = True)
    title = 'SD abs(#Heads - #Tails)' + numTrialsString
    makePlot(xaxis, diffSD, title, 'Number of Flips', 'Standard Deviation', 'bo', logX = True, logY = True)       
    title = 'Coeff. of Var. abs(#Heads - #Tails)' + numTrialsString
    makePlot(xaxis, diffsCVs, title, 'Number of Flips',
'Coeff. of Var.', 'bo', logX = True)
    title = 'Coeff. of Var. Heads/Tails Ratio' + numTrialsString
    makePlot(xaxis, ratiosCVs, title, 'Number of Flips', 'Coeff. of Var.', 'bo', logX = True, logY = True)    
    
    

flipPlot(4, 20, 20)  
