# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:07:23 2017

@author: User
"""
# first solution using zip
#drinkName = ['Mocha', 'Coffee', 'Iced Capp', 'Strawberry Smoothie', 'Steeped Tea', 'Hot Chocolate']
#drinkType = ['Hot', 'Hot', 'Cold', 'Cold', 'Hot', 'Hot']
#drinkPrice = [1, 1, 2, 3, 1, 1]
#
#zipped = zip(drinkName, drinkPrice, drinkType )
#print(list(zipped))

# another solution using myzip
a = ['Mocha', 'Coffee', 'Iced Capp', 'Strawberry Smoothie', 'Steeped Tea', 'Hot Chocolate']
b = ['Hot', 'Hot', 'Cold', 'Cold', 'Hot', 'Hot']
c = [1, 1, 2, 3, 1, 1]

def myzip(a,b,c):
    listofdrinks = []
    end = min(len(a), len(b), len(c))
    for i in range(end):
        listOf = []
        listOf.append(a[i])
        listOf.append(b[i])
        listOf.append(c[i])
        listofdrinks.append(listOf)
    return listofdrinks

print(myzip(a,b,c))
