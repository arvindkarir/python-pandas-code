# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:11:20 2018

@author: User
"""

orig = { 1:[2,5], 2:[3], 3: [1,5], 4: [] }
new = {}

for key, value in orig.items():
#    print(key)
    new[key] = []
#    print(new)
    for v in value:
        new[v] = []
#print(new)
for key, values in orig.items():
    for v in values:
        new[v].append(key)

print(new)
#
#
#for key, value in orig.items():
#    new[key] = []
#    for v in value:
#        new[v] = []
#
#for key value in orig.items():
#    for v in values:
#        new[v].append(key)