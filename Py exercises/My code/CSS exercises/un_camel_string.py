# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:45:00 2018

@author: User
"""

def un_camel(a_string): # convert from camelcase to uppercase
    uc_text = ''
    for x in a_string:
        if x.islower():
            uc_text += x.upper()
        else:
            uc_text += x
    print(uc_text)

un_camel('aBccDDefG')