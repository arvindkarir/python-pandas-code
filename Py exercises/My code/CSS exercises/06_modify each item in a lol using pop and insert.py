# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:35:53 2017

@author: User
"""

L = [[1,2], [35,4,78], [7,8,1,10],[2,3], [9,1,45]]

#def testA(L):
#    aFactor = 2
#    for m in L:
#        for ind, element in enumerate(m):
#            newElement = element*aFactor
#            m.pop(ind) # this works
#            m.insert(ind, newElement) # this works
#    return L
#
#print(testA(L))


# and this works as well
def testA(L):
    for m in L:
        for ind, element in enumerate(m):
            m[ind] *= 2
    return L

print(testA(L))