# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:43:28 2018

@author: User
"""

def drawfn(s, n):
    for i in reversed(range(n+1)):
        if i != 0:
#            print(i)
            print(s*i)
        if i ==0:
            print('='*10, end = "")
    for i in range(n+1):
        print(s*i)

drawfn('*',6)
drawfn('$',1)