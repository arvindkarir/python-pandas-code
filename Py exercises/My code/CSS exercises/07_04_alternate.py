# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:54:19 2018

@author: User
"""

def max_sum(l):
    if len(l) == 1:
        return(l)
    if len(l) == 2:
        max_of = max(sum(l), l[0], l[1])
        return int(max_of)
    else:
        middle_of_list = (len(l)//2)
        left_list = l[0:middle_of_list]
        right_list = l[middle_of_list:]
        print(left_list, right_list)
        max_left = max_sum(left_list)
        print(max_left)
        max_right = max_sum(right_list)
        print(max_right)
#        combo_list = max_left + max_right
#    print(combo_list)


def maxleftlist(ll):




#l = [9]
#l = [5,-5]
l =[-1,2,-5,1,3]
#l = [-2,1,-3,4,-1,2,1,-5,4]

print(max_sum(l))

