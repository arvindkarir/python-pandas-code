# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:49:25 2018

@author: User
"""

class Airlines():

    def __init__(self, code, date, fare):
        self.code = code
        self.date = date
        self.fare = int(fare)

    def getDates(self):
        print( self.date)

    def getFares(self):
        return int(self.fare)

    def Description(self):
        desc_str = [self.code + ', ' + self.date + ', ' + str(self.fare)]
        print (desc_str)

a = Airlines("airone", "11-12",100)
b = Airlines("airtwo", "12-20", 99)

a.Description()
a.getDates()
a.getFares()

b.Description()
b.getDates()
b.getFares()

def compFare(a, b):
    first = Airlines.getFares(a)
    second = Airlines.getFares(b)
    if int(first) < int(second):
        print('a is cheaper')
    else:
        print('b is cheaper')

compFare(a,b)