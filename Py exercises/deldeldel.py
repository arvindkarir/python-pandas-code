# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:11:20 2018

@author: User
"""

orig = { 1:[2,5], 2:[3], 3: [1,5], 4: [] }
new = {}

for key, value in orig.items():
    print(key)
    new[key] = []
    print(new)
    for v in value:
        new[v] = []
print(new)
for key, values in orig.items():
    for v in values:
        new[v].append(key)
#
print(new)
#
#first, second = [],[]
#
#for item in lol:
#    key = str(item[0])
#    value = str(item[1])
#    adict[key] = []







#for items in lol:
#    first.append(str(items[0]))
#    second.append(str(items[1]))
#
#newl = list(zip(first, second))
#for items in newl:
#print(newl)







#for key, value in adict.items():
##    for l in lol:
#    if key == l[0]:
#        adict[key] = [adict[key], value]



