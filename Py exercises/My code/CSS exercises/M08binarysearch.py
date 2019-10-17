# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:44:16 2018

@author: User
"""

def aSearch(L, target):
    start = 0
    end = len(L) -1
    while start <= end:
        middle = (start + end)//2
        if len(L) == 1:
            return L
        elif L[middle] == target:
            print('target:', target, 'at index:', middle)
            return True
        elif target < L[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return


L = [0,1,2,3,4,5,6]

print(aSearch(L, 6))