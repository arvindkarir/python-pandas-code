# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:05:53 2017

@author: User
"""
#without helper functions

def draw(a,b):
    c, d = 0, b
    for i in range(b):
        print(a*b)
        b -= 1
    if b == 0:
        print('============', end="")
    for i in range(d):
        print(a*c)
        c += 1




# with helper functions

#def draw(a,b):
#    updraw(a,b)
#    print('============')
#    downdraw(a,b)
#
#def updraw(a,b):
#    for i in range(b):
#        print(a*b)
#        b -= 1
#def downdraw(a,b):
#    c = 0
#    for i in range(b):
#        c += 1
#        print(a*c)


draw('~', 10)
draw('*', 12)
