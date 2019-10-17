# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:03:43 2017

@author: User
"""

import time

def testTime():
    start = int(round(time.time()*1000))
    for i in range(100000):
        multTable(5)
    end = int(round(time.time()*1000))
    print(end - start)

def multTable(n):
    table = [0]*n
    row = 0
    columns = list(range(n))
    print(table, columns)
    while row < n:
        this_row = []
        for c in columns:
            this_row.append((row+1)*(c+1))
        table[row] = this_row
        row = row + 1
    return table

testTime()

#print(multTable(5))