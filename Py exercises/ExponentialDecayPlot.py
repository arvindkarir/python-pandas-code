# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pylab

def clear(n, p, steps):
    """Assumes n & steps positive ints, p a float
    n: the initial number of molecules
    p: the probability of a molecule being cleared
    steps: the length of the simulation"""
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-p)**t))
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.yscale('log')
    pylab.title('Clearance of Drug')
    
clear(1000, 0.01, 1000)