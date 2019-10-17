# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:05:48 2018

@author: User
"""

def minval(a,b,c):
    smallest = 0
    if a < b and b < c:
        smallest = a
    if b < a and b < c:
        smallest = b
    else:
        smallest = c
    print(smallest)


minval(1,1,1)
minval(4,14,-3)