# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:59:04 2017

@author: User
"""
#import math
#
#def f1(x, meanV, stddeV):
#    tmpV = (1/(stddeV*((2*math.pi)**0.5)))
#    tmp2V = 1/(math.exp((x - meanV)**2/(2*stddeV**2)))
#    val = tmpV*tmp2V
#    return val
#print(f1(3.0, 5.0, 2.0))

#def forever_15():
#    n = input("your number\n")
#    n = int(n)
#    print(int((((n*3 + 45)*2)/6) - n))
#
#forever_15()

#    a = input("a\n")
#    b = input("b\n")
#    c = input("c\n")
#def max2(a, b):
#
#    k = a - b
#    m = (k >> 31) & 0x1
#    max = a - m*k
#    print(max)
#max2(240, -240)

def min3(a, b, c):
    minab = ((a+b)-abs(a-b))/2
    minabc = ((minab+c)-abs(minab-c))/2
    print(minabc)

min3(22, 66, 13)
