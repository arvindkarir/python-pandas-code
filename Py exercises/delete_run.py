# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 17:45:41 2017

@author: User
"""

def hailstone_2(n):
    if n == 0 or n ==1:
        print('1')
    elif n%2 == 0:
        print(n)
        hailstone_2(n//2)
    else:
        print(n)
        hailstone_2(3*n + 1)
 
hailstone_2(5)