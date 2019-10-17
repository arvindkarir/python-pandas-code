# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:39:22 2017

@author: User
"""

def convertNo(n, b):
    times = n//b
    divided = n%b
    if n == 0:
        return '0'
    elif times == 0:
        return str(divided)
    else:
        return convertNo(times, b) + str(divided)


print(convertNo(132234,3))