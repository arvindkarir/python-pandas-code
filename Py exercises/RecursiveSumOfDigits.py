# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:18:43 2017

@author: User
"""
def digitalSum(n):
    if n < 10:
      return n
    else:
      return n%10 + digitalSum(n//10)
  
print(digitalSum(1234331))
