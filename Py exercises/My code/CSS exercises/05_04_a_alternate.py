# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:30:06 2018

@author: User
"""

def digit_sum(n):
    if n < 10:
        return n
    else:
        return int(n%10) + digit_sum(int(n/10))

def is_square(n):
    a = digit_sum(n)
    digital_root_perfect = [1,4,7,9]
    total = 0
    for i in str(a):
        total += int(i)
    if total in digital_root_perfect:
        print('cannot decide')
    else:
        print('not a perfect square')



is_square(24008)
is_square(257)
is_square(144)
