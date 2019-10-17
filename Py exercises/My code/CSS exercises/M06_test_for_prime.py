# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:54:19 2018

@author: User
"""
def factorial(n):
    count_of = 1
    count_down = n
    n_fact = 1
    while count_of <=n:
#        print(count_of)
        n_fact *= count_of
        count_of += 1
    while count_down > 0:
#        print(count_down)
        count_down -= 1
    print(n_fact)


print(factorial(6))



#def prime_no(n):
#    test_factor = 2
#    while test_factor <n:
#        if n % test_factor == 0:
#            return False
#        else:
#            test_factor += 1
#    return True
#
#
#print(prime_no(59))