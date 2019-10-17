# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:35:12 2017

@author: User
"""

L = [[1,2], [35,4,78], [7,8,1,10],[2,3], [9,1,45]]

def testA(L):
    for m in L:
        for ind, element in enumerate(m):
            if element == 1:
                m.pop(ind)

    return L

print(testA(L))

