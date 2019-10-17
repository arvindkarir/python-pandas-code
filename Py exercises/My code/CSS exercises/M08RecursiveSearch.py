# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:44:18 2018

@author: User
"""

def aSearch(L, target):
    start = 0
    end = len(L) -1
    arecursion(L, target, start, end)

def arecursion(L, target, start,end):
    middle = (start + end)//2
    if L[middle] == target:
        print('target value',target,'at position', middle)
        return True
    elif target < L[middle]:
        end = middle - 1
    else:
        start = middle + 1
    return arecursion(L, target, start, end)

L = [0,1,2,3,4,5,6,7,8,9,11,13,16,17,20,22,25]

(aSearch(L, 20))
