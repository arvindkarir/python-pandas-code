# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 11:32:38 2017

@author: User
"""

def buildStr(los):
        if len(los) == 1:
            return los[0]
        else:
            return los[0] + buildStr(los[1:])

los = ['some thing', 'is', 'in', 'a', 'na me', 'of', 'a', 'great', 'war rior']

print(buildStr(los))


