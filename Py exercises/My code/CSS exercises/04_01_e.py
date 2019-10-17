# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:55:05 2017

@author: User
"""

m1=[1, 2, 23, 104]
m2=[-3, 2, 0, 6]

#mult_list (m1,m2) mutates m1 to [-3, 4, 0, 624]

def afn(m1, m2):
    start = 0
    newL = []
    bfn(m1, m2, start, newL)
    print(newL)

def bfn(m1, m2, start, newL):
    a, b = 0, 0
    if start == len(m1):
        return
    else:
        a = m1[start]
        b = m2[start]
        newL.append (a*b)
    bfn(m1, m2, start +1 , newL)


afn(m1, m2)