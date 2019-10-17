# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:12:50 2017
Big O of this implementation is the length of digits in m, so 10 steps for an m in billions
@author: User
"""

def gcd(m, n):

    if m < n: #we need n to be less than m
        (m,n) = (n,m)

    while (m%n) != 0: # as long as there is a remainder which is not zero
        (m,n) = (n, m%n) # get GCD of the remainder and n
    return(n)

print (gcd(112233445566778899,2346681))