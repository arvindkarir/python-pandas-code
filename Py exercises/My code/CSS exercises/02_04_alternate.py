# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:56:28 2018

@author: User
"""

def remainder(a,b):
    if a-b > b:
        newa = a-b
        remainder(newa,b)
    else:
        print(a-b)


remainder(1400,500)
