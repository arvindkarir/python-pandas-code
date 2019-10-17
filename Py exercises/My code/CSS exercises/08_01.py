# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:55:52 2018

@author: User
"""
def sumLists(L):
    LOL = lolSum(L)
    LOLnew = []
    for i in LOL:
        if i ==0:
            LOLnew.append(i)
        elif i >0:
            i = i*2
            LOLnew.append(i)
        else:
            i = i*i
            LOLnew.append(i)
    return LOLnew


def lolSum(L):
    lolSum = []
    for i in L:
        sumOf = 0
        for j in i:
            sumOf += j
        lolSum.append(sumOf)
    return lolSum


print(sumLists([[1, 2, 3], [3, 2, -8], [1, 3, -4]]))