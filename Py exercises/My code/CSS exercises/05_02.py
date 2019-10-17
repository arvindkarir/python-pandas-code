# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:34:39 2017

@author: User
"""
#def fibOf(n):
#    if n ==0:
#        return 0
#    else:
#        return fibRe (n, 1, [0,1])
#
#def fibRe(n, n0, fibs):
#    if n0 >= n:
#        return fibs[-1]
#    else:
#        fibs.append(fibs[-1] + fibs[-2])
#        return fibRe(n, n0+1, fibs)
#
#print(fibOf(10))
#########################
def fact(n):
    return stepFac(1,n)

def stepFac(product, end):
    if end <= 1:
        return product
    else:
        return stepFac(product*end, end-1)

print(fact(3))
#########################
def sumOf(n):
    return stepSum(1,n)

def stepSum(totalOf, endOf):
    if endOf <= 1:
        return totalOf
    else:
        return stepSum(totalOf + endOf, endOf-1)

print(sumOf(3))
#########################

def computeEq(n):
        vals = 1
        computeVals(n, vals)

def computeVals(n, vals):
    if n == 0:
        return vals
    else:
        vals = sumOf(n)/fact(n) + vals
        print(vals)
        computeVals(n-1, vals)

(computeEq(3))