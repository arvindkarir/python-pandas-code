# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 12:46:00 2018

@author: User
"""
######## stripping brackets##
#aString = "((3+5)))+(8)"
#def isValid(aString):
#    for num, char in enumerate(aString):
#        if char =="(":
#            pos1 = num
#        if char ==")":
#            pos2 = num
#    newString = aString.replace(aString[pos1], "")
#    newString = newString.replace(aString[pos2], "")
#    print(newString)
#isValid(aString)
##############################
#from functools import reduce
#def isValid(aString):
#    splitString = (aString.split("()"))
#    print(splitString)
#    print(reduce(lambda a,b: a + b, splitString))
######################
## counts the brackets
#def isValid(aString):
#    posCount = 0
#    openBr = 0
#    for posCount in range(len(aString)):
#        if aString[posCount] == '(':
#            openBr += 1
#        elif aString[posCount] == ')':
#            openBr -= 1
#        if openBr == 0:

#######################
#import re
#def isValid(aString):
#    print(re.sub(r'()', '', aString)) # splits the string by brackets
#################
import re

def isValid(aString):
    aSet = set(['1','2','3','4','5','6','7','8','9'])
    newString = re.sub(r'()', '', aString)
    print('here it is',newString)
    if aString == "":
        print('False')
    elif aString in aSet:
        print('True')
    else:
        if aString[0] == '(' and aString[len(aString)-1] == ')':
            print('True')
        else:
            print('False')

isValid("")
isValid("3")
isValid("(6+4)")
isValid("((6+4)+8)")
isValid("(6+4)+8")
isValid("((3+5)+(8+7))")
isValid("((5 + 3) + (3 + 2)) + (2 + ((1 + 1) + 0))")