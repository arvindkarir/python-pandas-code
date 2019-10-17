# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:20:00 2017
Different values of maxWeight yields different answers 
@author: User
"""

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ',' + f"{(self.value)}" + ',' + f"{self.weight}" + '>' #use of f{"variable"} for float, else typeError
        return result
    
# dictionaries can be used as well, did not try it yet
#        dict = { 'items':['clock', 'painting', 'radio', 'vase', 'book', 'computer'],'values': [175,90,20,50,10,200], 'weights': [10,9,4,2,1,20]}
#print(list(dict.keys())) --> prints the keys
#print(list(dict.values())) --> prints the list of list of values
    
def value(item):
    return item.getValue()
def weightInverse(item):
    return 1.0/item.getWeight()
def density(item):
    return item.getValue()/item.getWeight()

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
        print(Items[i]) #prints each i of Items
    print(end="\n") #this inserts a new line after printing ALL Items
    return Items

def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse = True)
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
            print(totalWeight, totalValue)
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction) #greedy returns two things in return - result and totalValue. result is a list of items taken and total value, assigned here
    print ('Total value of items taken = ', val)
    for item in taken:
        print( ' ', item)
        
def testGreedys(maxWeight = 34):
    items = buildItems()
    print( 'Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, value)
    print ('\nUse greedy by weight to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, weightInverse)
    print ('\nUse greedy by density to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, density)

testGreedys()