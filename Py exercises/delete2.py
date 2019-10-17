# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:22:30 2018

@author: User
"""
#def new_sort(l):
#    for j in range(len(l)):
#        key = l[j]
#        i = j-1
#        while i > -1 and l[i] < key:
#            l[i+1] = l[i]
#            i = i -1
#        l[i+1] = key
#    print(l)
#
#l = [5,2,4,6,1,3]
#new_sort(l)

def binary_add(s1, s2):
    result = key =  ''
    carryover = 0
    len_1 = len(s1)
    len_2 = len(s2)
    if len_1 > len_2:
        big_no = s1
        small_no = s2
    else:
        big_no = s2
        small_no = s1
    for i in range(len(big_no)-len(small_no)):
        small_no = '0' + small_no
    print(small_no, big_no)
    for i in range(len(big_no) - 1, -1, -1):
        if big_no[i] == '1'and small_no[i] == '1' and carryover ==1:
            key = '1'
            carryover = 1
        if big_no[i] == '0'and small_no[i] == '1' and carryover ==1:
            key = '0'
            carryover = 1
        if big_no[i] == '1'and small_no[i] == '0'and carryover ==1:
            key = '0'
            carryover = 1
        if big_no[i] == '0'and small_no[i] == '0'and carryover ==1:
            key = '1'
            carryover = 0
        if big_no[i] == '0'and small_no[i] == '0'and carryover ==0:
            key = '0'
            carryover = 0
        if big_no[i] == '1'and small_no[i] == '0'and carryover ==0:
            key = '1'
            carryover = 0
#        if big_no[i] == '1'and small_no[i] == '1'and carryover ==0:
#            key = '1'
            carryover = 1
        if big_no[i] == '0'and small_no[i] == '1'and carryover ==0:
            key = '1'
            carryover = 0

        result = result + key
    if carryover == 1:
        result = '1' + result
    print (result)

s1 = '100'
s2 = '110101'
(binary_add(s1, s2))
#
#def addsth(l):
#    combo = ''
#    for i in l:
#        combo += i
#    print(combo)
#
#l = '11010kk1'
#addsth(l)

