# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:45:30 2017

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

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total weight of a solution to the
    0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0: #nothing left to consider, no more available wt.
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        result = maxVal(toConsider[1:], avail) #Explore right branch ONLY, move over to the next item as the weight is exceeded with [0]
    else:
        nextItem = toConsider[0] #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight()) #chosen the [0] item, now run function with [1:] items
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def smallTest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxVal(Items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken =', val)


















#def BuildItems():
#    names = ['a','b','c','d']
#    values = [6, 7, 8, 9]
#    weights = [3, 3, 2, 5]
#    Items = []
#    for i in range(len(values)):
#        Items.append(Item(names[i], values[i], weights[i]))
#        print(Items[i])
#    print(end="\n")
#    return Items
#        
        
        
        
        
        