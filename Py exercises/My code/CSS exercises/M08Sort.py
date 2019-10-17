# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:37:57 2018

@author: User
"""

def newSort(L):
    n = len(L)
    positions = list(range(n-1))
    for i in positions:
        minpos = i
        for j in range(i, n):
            if L[j] < L[minpos]:
                minpos = j
        temp = L[i]
        L[i] = L[minpos]
        L[minpos] = temp


alist = [4,5,2,1,3,2,5,4,7]

newSort(alist)
print(alist)