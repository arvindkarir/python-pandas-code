# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 12:46:00 2018

@author: User
"""

def findSub(expr):
        e = expr[1:-1].replace(' ','')
#        print(e)
        countBr = 0
        for x in range(len(e)):
            if e[x] == '(':
                countBr += 1
            elif e[x] == ')':
                countBr -= 1
            if countBr == 0:
                rightE = e[x+2:]
                leftE = e[:x+1]
                if x == len(e) -1:
                    operator = '$$'
                else:
                    operator = e[x+1]
#                print(e, operator)
#                print('l',leftE,':','r',rightE)
                return leftE, rightE, operator

def isValid(aString):
    baseExpr = list(map(str, (range(1,10))))
    if len(aString) ==1 and aString in baseExpr:
        return True
    if aString == "":
        return False
    if aString[0] != '(' and aString[-1] != ')':
        return False
    l, r, operator = findSub(aString)
    if operator != '+':
        return False
    return isValid(r) and isValid(l)

print(isValid(""))
print(isValid("3"))
print(isValid("(6+4)+8"))
print(isValid("((6+4)+8)"))
print(isValid("((3+5)+(8+7))"))
print(isValid("(((5 + 3) + (3 + 2)) + (2 + ((1 + 1) + 5)))"))
print()
#true_cases = [
#  '(5 + 3)',
#  '((5 + 2) + 3)',
#  '(5 + (3 + 2))',
#  '(((1 + 2) + 5) + (1 + (2 + 3)))',
#  '1',
#  '(1 + (1 + (1 + (1 + (1 + 1)))))'
#]
#false_cases = [
#  '1 + 2',
#  '',
#  '1 + (1 + 2)',
#  '(1 + (2 ( (2 + 3)))',
#  '(0 + 1)',
#  'P1 + 2C',
#  '((1 + 2))',
#  '(1 * (2 + 2))'
#]
#
#for expr in true_cases:
#    if not isValid(expr):
#        print('Algo failed, cuz returned False in true_cases', expr)
#
#for expr in false_cases:
#    if isValid(expr):
#        print('Algo failed', expr)