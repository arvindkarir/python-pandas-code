# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 17:23:17 2017

@author: User
"""

aList = ['a', 'b', 'c', 'd', 'e', 'f','g']

#
#def groupNames(aList, n):
#    if len(aList) <=n:
#        return aList
#    else:
#        lolGroup = [aList[0:n]]
#        newL = aList[n:]
#        lolGroup += (groupNames(newL, n))
#    return lolGroup

## Another way without recursion, still in process
#def groupNames(aList, n):
#    lolGroup = []
#    for i in range(0, len(aList),n ):
#        lolGroup.append([aList[i:i+n]])
#    return lolGroup

# Yet another way, thanks Amour!!
def groupNames(aList, n):
    return [aList[i:i+n] for i in range(0, len(aList),n )]

print(groupNames(aList, 3))

# An example of a complex statement
#a = [i**2 for i in range(5)]
#print(a)