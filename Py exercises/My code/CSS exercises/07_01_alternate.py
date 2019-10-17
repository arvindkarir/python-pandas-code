# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:52:54 2018

@author: User
"""

def tobase3(n):
    ternary = (n%3)
    balance = (n//3)
    if n == 0:
        return '0'
    elif balance == 0:
        return str(ternary)
    else:
        return tobase3(balance) + str( ternary)


print(tobase3(13))