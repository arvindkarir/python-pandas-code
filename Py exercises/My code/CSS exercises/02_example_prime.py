# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:32:47 2018

@author: User
"""

def isprime(n):
    if n < 2:
        return False
    else:
        for x in range(2,n):
            if n%x == 0:
                return False
        return True




print(isprime(21))