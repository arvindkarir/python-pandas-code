# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 18:29:24 2017

@author: User
"""

def multVals(vals, multiplier):
    newVals = []
    for elements in vals:
        newVals.append(elements*multiplier)
    vals[:] = newVals # this is the way to change a global variable vals to the new values. If just vals is used then global is unchanged. so use 'vals[:]'


vals = [1,2,3,4,5,6,7,8,9,11,44,55,222]

print(multVals(vals, 10))
print(vals)
