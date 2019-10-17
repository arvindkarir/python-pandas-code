# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:37:41 2018

@author: User
"""

mylist = [x*x for x in range(3)]
print(mylist)
for i in mylist:
    print(i)

mygenerator = (x*x for x in range(3))
print(mygenerator)

for i in mygenerator:
    print(i)

