# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:46:44 2017

@author: User
"""

def drawDi(a):
    b = a
    m,n = 1,2
    for i in range(a):
#        print('a', a, 'i', i)
        print(' '*(a-i),'$'*(i+m))
        m += 1
    for j in range(b-1):
        print(' '*(j+2),'$'*(2*(b-n)+1))
        n += 1

drawDi(5)
drawDi(12)