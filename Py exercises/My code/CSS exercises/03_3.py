# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:16:16 2017

@author: User
"""
import re

def passCheck(pwd):
    flagOne, flagTwo, flagThree = False, False, False
    score = 0
#    print('Enter a password with one uppercase, one lowercase, one digit.\n')
#    pwd = input('Password is...')
    if re.search(r'[A-Z]', pwd):
        flagOne = True
    if re.search(r'[a-z]', pwd):
        flagTwo = True
    if re.search(r'[0-9]', pwd):
        flagThree = True
    if  flagOne==True and flagTwo==True and flagThree==True:
        print('password accepted')
    spls = re.findall(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', pwd)
    splCount = len(spls) - 1

    if len(pwd) < 5:
        score -= 10
    if len(pwd) > 8:
        score += 15
    if splCount >= 1:
        score += 10*splCount
    return score


print(passCheck('Xy 37 1-0'))
print(passCheck('Password999'))
print(passCheck('Yt3)(*&a%'))
print(passCheck('PaSsWoRd'))










