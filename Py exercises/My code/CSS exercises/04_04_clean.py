# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:44:09 2017
@author: User
"""

# Amour's solution
conversions = [' ', '.,?', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']



def compose_msg(keypresses):
  return ''.join(map(lambda x: conversions[x[0]][x[1]-1], keypresses))

print(compose_msg([[6,3], [0,1],[5,2]]))
