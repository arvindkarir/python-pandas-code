# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:10:59 2018

@author: User
"""

def username():

    first = 'arvind' #input('firstname')
    last = 'KARIR' # input('lastname')
    (yob) = str(1234) #int( input('yob') )
    yob = yob[:3]
    last = last[-4:]

    print(first[:1].lower()+last.upper()+ yob[::-1])

username()