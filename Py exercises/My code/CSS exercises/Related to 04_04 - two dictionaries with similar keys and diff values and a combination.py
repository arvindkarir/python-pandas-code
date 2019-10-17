# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 19:36:04 2017

@author: User

Look up two dictionaries with similar keys
and consolidate the values

"""
d1 =  {1:'a', 2:'b', 3: 'c', 4:'d'} # first dict
d2 = { 1: 'A',2:'B', 3:'C', 5:'E'} # second dict
consol_dict = {} # final dict
for k in d1: # just testing
    print(k, d1[k]) # print key and its value

dd1k = set(list(d1.keys())) # a set of d1 keys
dd2k = set(list(d2.keys())) # a set of d2 keys

dd = list(dd1k & dd2k) # intersection of two key sets
dd1 = list(dd1k - dd2k) # diff of d1 minus d2 - values in d1 only
dd2 = list(dd2k - dd1k) # values in d2 only

print(dd, dd1, dd2) # testing

for k in dd: # getting vals for both d1 and d2
    print('d1,d2', d1[k] + d2[k])
    consol_dict[k] = d1[k] + d2[k]

for k in dd1: # vals for keys in only d1
    print('d1-d2', d1[k])
    consol_dict[k] = d1[k]

for k in dd2: # vals for key in only d2
    print('d2-d1', d2[k])
    consol_dict[k] = d2[k]

print(consol_dict) # yay!!