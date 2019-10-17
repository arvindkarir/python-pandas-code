# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:15:00 2018

@author: User
"""

## find max list 07_04
#
#testList = [-2,1,-3,4,-1,2,1,-5,4]
#aList = [-1,2,-5,1]
##aList = [1, 2, 3]
#
#def maxSum(lst, left, right):
#    leftSum = 0
#    rightSum = 0
#    maxLeft = 0
#    maxRight = 0
#
#    middle = (left + right)//2
#
#    if left == right:
#        if lst[left] > 0:
#            return lst[left]
#        else:
#            return 0
#
#    maxLeft = maxSum(lst, left, middle)
#    maxRight = maxSum(lst, middle+1, right)
#
#    return max(maxLeft, maxRight)
#
#print(maxSum(testList, 0, 8))


#testList = [-1,2,-5,1]

testList = [1, -2 ,3,6,-3,-1,6,-5]

def maxList(lst, start, end):
    maxLeft, maxRight = 0, 0
    leftSum, rightSum = 0, 0
    middle = (start + end)//2

    if start == end: # for middle value
        return max(lst[start], 0)

    maxLeftlist = maxList(lst, start, middle)
    maxRightlist = maxList(lst, middle+1, end)

    for i in range(middle, start-1, -1):
        leftSum = leftSum + lst[i]
        if leftSum > maxLeft:
            maxLeft = leftSum
    for i in range(middle+1, end+1):
        rightSum = rightSum + lst[i]
        if rightSum > maxRight:
            maxRight = rightSum

    return max(maxLeft + maxRight,maxLeftlist, maxRightlist)


print(maxList(testList, 0, len(testList)-1))