# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:18:47 2017
https://www.youtube.com/watch?v=CB_NCoxzQnk --- for choosing a good pivot point

https://www.youtube.com/watch?v=AJSiJtwc8EE --- for most of the code
@author: User
"""
import random

def mySort(listTo, lowI, highI):
    if ((highI - lowI) >0): # If the list is one element only, then return
        p= partition(listTo, lowI, highI) # divide the list into two parts based on partition function
        mySort(listTo, lowI, p-1) # sort the low end of list
        mySort(listTo, p+1, highI) # sort the high end of list

def getPivot(listTo, lowI, highI): # getting a right pivot is important, here we choose a median value
    mid = (lowI + highI)//2 # pick an item in the middle
    pivot = highI # arbitrarily assign pivot to be the high index
    if listTo[lowI] < listTo[mid]: # if low <mid < high, then pivot is good
        if listTo[mid] < listTo[lowI]:
            pivot = mid
    elif listTo[lowI] < listTo[highI]: # mid is not in middle (it is in beginning), go with beginning
        pivot = lowI
    return pivot # return the pivot value

def partition(listTo, lowI, highI): # this function does most of the work
    pivotI = getPivot(listTo, lowI, highI) # get the pivot value
    border = lowI # set the border
    for i in range(lowI, highI):
        if listTo[i] < listTo[pivotI]: #if the element is less than pivot value
            listTo[i], listTo[border] = listTo[border], listTo[i] # then swap
            border += 1 # increment border, ie shift to right
    listTo[pivotI], listTo[border] = listTo[border], listTo[pivotI] # once the loop is complete, switch border and pivot
    return border

test1 = random.sample(range(0,10000), 1000)
#print(test1)
mySort(test1, 0, 999) # NOTE to change this highI as well corresponding to the len(listTo)
print('sorted list is', test1)