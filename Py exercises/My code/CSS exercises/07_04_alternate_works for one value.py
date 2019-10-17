# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:54:19 2018

@author: User
"""

def max_sum(l):
    combolist= maxl = maxr = []
    middle_of_list = (len(l)//2)
    left_list = l[0:middle_of_list]
    right_list = l[middle_of_list:]
    print(left_list, right_list)
#    if len(left_list) == 1:
#        combolist.append(left_list)
#    if len(right_list) == 1:
#        combolist.append(right_list)
    if len(left_list) == 2:
        combolist.append(max_left_list(left_list,maxl))
    if len(right_list) == 2:
        combolist.append(max_right_list(right_list,maxr))
    else:
        print(left_list, right_list)
        max_sum(left_list), max_sum(right_list)
    print(combolist)

def max_left_list(l,maxl):
    if l[0] > l[1]:
        maxl = l
    else:
        maxl = l[1]
    return maxl

def max_right_list(l,maxr):
    if l[0] > l[1]:
        maxr = l[0]
    else:
        maxr = l
    return maxr


l =[-1,2,-5,1]
#l = [-2,1,-3,4,-1,2,1,-5,4]
(max_sum(l))

