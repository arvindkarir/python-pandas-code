# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:23:33 2018

@author: User
"""

def bin_add(n1, n2):
    binary_sum = ''
    carry = '0'
    len_1 = len(n1)
    len_2 = len(n2)
    if len_1 > len_2:
        big_no = n1
        small_no = n2
    else:
        big_no = n2
        small_no = n1
    for i in range(len(big_no)-len(small_no)):
        small_no = '0' + small_no
    print(small_no, big_no)
    for i in range(len(big_no)-1, -1,-1):
        if ( (int(big_no[i]) + int(small_no[i]) + int(carry) ) ) == 0:
            print('0')
            carry = '0'
            binary_sum += str(0)
        if ( (int(big_no[i]) + int(small_no[i]) + int(carry) ) ) == 1:
            print('1')
            carry = '0'
            binary_sum += str(1)
        if ( (int(big_no[i]) + int(small_no[i]) + int(carry) ) ) > 1:
            print('1')
            carry = '1'
            binary_sum += str(1)
    print( ''.join(reversed(binary_sum) ) )




n1 = '10001101'
n2 = '11110'

bin_add(n1, n2)