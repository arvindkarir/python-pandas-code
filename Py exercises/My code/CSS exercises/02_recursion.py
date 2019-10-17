# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:32:47 2018

@author: User
"""

#def sumpowers(b,n):
#    if n == 0:
#        return 1
#    else:
#        return b**n + (sumpowers(b,(n-1) ) )
#
#print(sumpowers(5,3))



def isprime(n):
    if n < 2:
        return False
    else:
        for x in range(2,n):
            if n%x == 0:
                return False
        return True




print(isprime(21))