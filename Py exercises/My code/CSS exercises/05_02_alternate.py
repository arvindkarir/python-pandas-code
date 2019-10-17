# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:51:16 2018

@author: User
"""

def compute_eq(n):
    if n == 0:
        subtotal = 1
        return subtotal
    else:
        values = list(range(1,n+1))
        top = sum(values)
        bot = 1
        for x in values:  # could be achieved by factorial function in math module perhaps
            bot *= x
            subtotal = top/bot + compute_eq(n-1)
    return(subtotal)

print(compute_eq(3))
print(compute_eq(1))
#print(compute_eq(10))