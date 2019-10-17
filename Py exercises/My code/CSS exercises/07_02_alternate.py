# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:50:35 2018

@author: User
"""

def group(l, n):
    lol = []
    for i in range(0, len(l), n):
        lol.append(l[i: i+n])
    print(lol)


group(["James", "Kate", "Lee", "Anna"], 3)