# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:35:43 2018

@author: User
"""

class Robot(object):

    def __init__(self, name = None, buildYear = None):
        self.name = name
        self.buildYear = buildYear

    def sayHi(self):
        if self.name:
            print('Hi, I am ' + self.name)
        else:
            print('Use setName method to give me a name')

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setYear(self, by):
        self.buildYear =by

    def getYear(self):
        return self.buildYear


x = Robot()
Robot.brand = 'kuka'
y = Robot()
x.setName('mokavoka')
y.brand = 'Muka'
x.brand = 'JJuka'
y.setName(x.getName())
print(y.getName())
x.sayHi()
y.setYear(2020)
print(y.getName() + " was created in", y.getYear())
