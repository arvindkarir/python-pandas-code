# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:01:58 2018

@author: User
"""

def insertionSort(L):
    for i in range(1, len(L)):
        insert (L, i)

def insert(L, pos):
    while pos > 0 and L[pos] < L[pos-1]:
        temp = L[pos]
        L[pos] = L[pos-1]
        L[pos-1] = temp
        pos = pos-1


aList = [5,8,2,4,3,3,1,11,9,6]
insertionSort(aList)
print(aList)