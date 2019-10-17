# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:18:52 2017

@author: User
"""


def digitSum(n):
        if n <=9:
            return n
        else:
            return n%10 + digitSum(int(n/10))

def isSquare(n):
    aTotal = digitSum(n)
    if aTotal >= 9:
        aTotal = digitSum(aTotal)
        printString(aTotal)


def printString(vals):
    if vals ==1 or vals ==4 or vals ==7 or vals ==9:
        print('cannot decide')
    else:
        print('not a perfect square')

(isSquare(257))