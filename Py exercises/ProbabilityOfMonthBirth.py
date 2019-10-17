# -*- coding: utf-8 -*-
"""
Spyder Editor
Calculate the probability of more than 46 births in any month for 446 births. 446/12 is around 37, and 46 births means 30% more than 'average rate'
This is a temporary script file.
"""
import random

def anyMonth(numTrials):
    any48 = 0
    for j in range(numTrials):
        monthB = 0
        for i in range(446):
            if random.randint(1,12) == 6:
                monthB += 1
        if monthB >= 46:
             any48 += 1
    mProb = any48/float(numTrials)
    
    print('more than 48 births prob for any month', mProb)
             
anyMonth(100)            
            