# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:51:06 2017

@author: User
"""

def fun(n, x, l):
    if x%n==0:
         l.append(n)
    if n==1:
         return None
    fun(n-1, x, l)


def divisibles(n):
    x = n
    l = []
    if n == 0:
        l = []
    elif n ==1:
        l = []
    else:
        fun(n-1, x, l)
    print(l[::-1])

divisibles(0)
divisibles(1)
divisibles(16)
divisibles(19)