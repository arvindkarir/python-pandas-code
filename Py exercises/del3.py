# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 23:33:44 2018

@author: User
"""

def swappedDict(source):
    swapped = {}
    for k, v in source.items():
        if v not in swapped:
            swapped[v] = set()
        swapped[v].add(k)
    return swapped


source = {'Europa': 'Jupiter', 'Psamathe': 'Neptune', 'Cordelia': 'Uranus', 'Cupid': 'Uranus'}

print(swappedDict(source))