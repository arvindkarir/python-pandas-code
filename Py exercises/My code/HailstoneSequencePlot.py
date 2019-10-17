# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:07:01 2017
Yay, this program plots hailstone values for a range
And it saves each figure plus each sequence as a csv file
some other plot commands for reference
# pylab.ylim(0,5000) #limits can work as well, but errors
# pylab.xlim(100, 0) #reversing the axis

import matplotlib.pyplot as plt
# plt.gca().invert_xaxis() # this reverses the x-axis but only till n = 19 or 29 or 39, then switches!!

@author: User
"""
import pylab
import numpy as np

def hailstone_seq(countFrom, countTo):
    n = countFrom
    for n in range(countFrom, countTo + 1):
        seq = [n]
        if n < 1:
           return []
        while n > 1:
           if n % 2 == 0:
             n = n / 2
           else:
             n = 3 * n + 1 
           seq.append(n)
        printSeq(seq) #The indentation level of this command is important, diff between printing for each output of n vs the series, move it and try!!
    countFrom += 1 # this is important for returning the value else always stuck in a loop
           
def printSeq(theseq):
    revSeq = theseq[::-1] #reverses the sequence so all of them start with 1, 2, 4 ...
    print(revSeq) #just for debugging          
    pylab.plot(revSeq, linewidth = 1) #plots one of top of another
    pylab.title('Hailstone values up to %s' %theseq[0]) # extracts first value of last sequence, which is countTo           
    pylab.savefig('C:\\Users\\User\Desktop\MIT EdX programming course\Py exercises\data_dump\{0}fig'.format(theseq[0]))
    np.savetxt('C:\\Users\\User\Desktop\MIT EdX programming course\Py exercises\data_dump\{0}data.csv'.format(theseq[0]), theseq, delimiter=",", fmt='%s')                   
    
hailstone_seq(3,10)