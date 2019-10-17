# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:02:23 2018

@author: User
"""

def is_valid(s):
# catching the two easiest conditions
    if s == '':
        return (False)
    elif s in ['1','2','3','4','5','6','7','8','9','0']:
        return (True)
    elif s.count('(') == 0: # if above conditions are not met and there is no beginning parenthesis, then False
        return False
    else:
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')' and stack:
                stack.append(i)
        if stack[-1] != len(s)-1: #if parentheses don't match then issue
            return False
    return True


print(is_valid ("") )# False
print(is_valid ("3") )# True
print(is_valid('1 + 2')) #False
print(is_valid( '(1 + (2 ( (2 + 3)))) ') ) #False
print(is_valid('(5 + 3)')) #True
#print(is_valid('1'))
#print(is_valid('1'))

#is_valid ("(3+5)+8") # False
#is_valid ("(6+4)") # True
#is_valid ("((3+5)+8)") # True
#is_valid ("((3+5)+(8+7))") #True

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

############################################


#for expr in true_cases:
#    if not is_valid(expr):
#        print('Algo failed, cuz returned False in true_cases', expr)
#
#for expr in false_cases:
#    if is_valid(expr):
#        print('Algo failed', expr)

##################################################
#else:
#    the_value = eval(eval('s'))
#    try:
#        int(the_value)
#        print(True)
#    except ValueError:
#        print(False)

#    start_brackets = s.index('(')
#    end_brackets = s.index(')')
#    print(start_brackets, end_brackets)


#    print(s.find(')') ,len(s))

#    val = s.split('(')[1].split(')')[0]
#    print(val)