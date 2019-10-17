# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:47:46 2018

@author: User
"""

def sum_lists(l):
    final_list = []
    for eachlist in l:
        print(eachlist)
        sub_total = 0
        for each in eachlist:
            print(each)
            sub_total += int(each)
        print(sub_total)
        if sub_total >=0:
            sub_total *= 2
        if sub_total <0:
            sub_total = sub_total**2
        final_list.append([sub_total])
    print(final_list)



l = [[1, 2, 3], [3, 2, -8], [1, 3, -4]]
sum_lists(l)