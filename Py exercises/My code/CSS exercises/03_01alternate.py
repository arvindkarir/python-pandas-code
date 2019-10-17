# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:13:02 2018

@author: User
"""

def checkit(s1, s2):
    for i in s1:
        for j in s2:
            if i == j:
                s1 = s1[1:]
                s2 = s2[1:]
                print(i,j, s1, s2)
                if len(s1) >=1 and len(s2) ==0:
                    return True
    return False


print(checkit("I am a string","I am a"))