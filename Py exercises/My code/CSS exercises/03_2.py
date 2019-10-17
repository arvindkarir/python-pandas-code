# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:30:46 2017

@author: User
"""

def makeName():
#    commonS = []
    s1 = str(input('Enter your first name\n'))
    s2 = str(input('Enter your last name\n'))
    s3 = str(input('Enter your year of birth YYYY\n'))
    print('This is what you entered\n', s1,'\n', s2, '\n', s3)
    onebit = s1[0].lower()
    twobit = s2[-4:].lower()
    lastbit = s3[::-1]
    lastbitRev = lastbit[1:4]
    print(onebit + twobit + lastbitRev)

makeName()
