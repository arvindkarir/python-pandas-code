# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:43:28 2018

@author: User
"""

def drawfn(n):
    spaces = n
    for i in range(1,2*n,2):
        print(' '*spaces,'$'*i)
        spaces -= 1
    spaces = 2
    for i in reversed(range(1,2*(n-1),2)):
        print(' '*spaces,'$'*i)
        spaces += 1


drawfn(8)
#drawfn(1)