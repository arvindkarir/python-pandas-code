# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 13:30:10 2017

@author: User
"""

def afn(lst, val, newVal):
    start = 0
    count = 0
    bfn(lst, start, val, newVal, count)
    print(lst, count)

def bfn(lst, start, val, newVal, count):
    if start == len(lst):
        return
    if (lst[start]) == val:
        (lst[start]) = newVal
        count += 1
    bfn(lst, start + 1, val, newVal, count)

lst = [3, 10, 5, 10, -4]
afn(lst, 10, 77)
