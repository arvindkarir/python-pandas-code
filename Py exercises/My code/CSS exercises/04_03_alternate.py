# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:30:14 2018

@author: User
"""

def compose_msg(keypresses):
    message = ''
#    phonedigits = ['0','1','2','3','4','5','6','7','8','9']
    phonechrs = [' ','.,?','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    for eachpress in keypresses:
        a = (eachpress[0])
        b = (eachpress[1])
#        print(a,b)
        message += (phonechrs[a][b-1])
    print(message)

compose_msg([[6, 3], [0, 1], [5, 2]])