# -*- coding: utf-8 -*-
"""
Random Walk exercise
Two major problems with original code were in int calls
solved by math.fsum and def of a totalofString function
"""
import random
import pylab
import math

def CV(X):
    mean = math.fsum(X)/float(len(X)) #original code called for mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')
    
def stdDev(X):
    mean = math.fsum(X)/len(X) #original code called for mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5 #Square root of mean difference

# ------------get the necessary definitions and imports out of the way ----------------

class Location(object):
    def __init__(self, x, y): #x, y are floats
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self, x):
        return self.x
    
    def getY(self, y):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox #no need for abs since squared below
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
    
class Field(object):
    
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
                raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]     
    
class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name
    
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'
    
def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0. Moves d numSteps times, and returns the difference between the final location and the location at the start of the walk."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int >= 0, numTrials an int > 0, dClass a subclass of Drunk. Simulates numTrials walks of numSteps steps each. Returns a list of the final distances for each trial"""
    Homer = dClass()
    origin = Location(0.0, 0.0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(walk(f, Homer, numSteps))
    return distances
    
def drunkTest(walkLengths, numTrials, dClass):
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', math.fsum(distances)/len(distances), 'CV =', CV(distances)) #changing to math.fsum(distances) from sum(distances) solved the problem
        print(' Max =', max(distances), 'Min =', min(distances))
 

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)       

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
    
class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
    
drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)

#def simAll(drunkKinds, walkLengths, numTrials):
#    for dClass in drunkKinds:
#        drunkTest(walkLengths, numTrials, dClass)
        
#simAll((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)

class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
        
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result

# ------------Needed to add this function as cvs and mean were lists of lists and needed a summation-----------
def totalofString(items): 
    totalist = 0
    for element in items:
        if type(element) == type([]):
            totalist = totalist + totalofString(element)
        else:
            totalist = totalist + element
    return totalist
# -----------------------------------------------------------------------------------------------
    
def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    cvDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
#        print(trials)
        mean = totalofString(trials)/float(len(trials))
        meanDistances.append(mean)
        cvDistances.append(stdDev(trials)/mean)
    return (meanDistances, cvDistances)

def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('b-', 'r:', 'm-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
#        print('Starting simulation of', dClass.__name__means, cvs = simDrunk(numTrials, dClass, walkLengths)) -->this line still AttributeError
        cvs = simDrunk(numTrials, dClass, walkLengths)
#        print('cvs is:', totalofString(cvs))
        cvMean = totalofString(cvs)/len(cvs)
        pylab.plot(walkLengths, curStyle, label = dClass.__name__ + '(CV = ' + str(round(cvMean, 4)) + ')')

    pylab.title('Mean Distance from Origin ('  + str(numTrials)+ 'trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
    pylab.semilogx()
    pylab.semilogy()
    

simAll((UsualDrunk, ColdDrunk, EWDrunk), (10,100,1000), 100)

