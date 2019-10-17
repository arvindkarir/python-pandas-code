# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 13:30:10 2017

@author: User
"""

def a(n):
      if n == 0:
            return []
      if n == 1:
            return [[1]]
      return a(n-1) + [list(range(1,n+1))]


print(a(5))