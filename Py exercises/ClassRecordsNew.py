# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:29:49 2017

@author: User
"""
import datetime

class Person(object):
    
    def __init__(self, name):
        '''create a person'''
        self.name = name
        try:
            lastBlank = name.rindex(' ') #returns the index of last space
            self.lastName = name[lastBlank+1:] #strips away the last string after last space, presumably the last name
        except:
            self.lastName = name #if only one name is input, considered last name
        self.birthday = None
        
    def getName(self):
        """returns self's full name"""
        return self.name
    
    def getLastName(self):
        return self.lastName
    
    def setBirthday(self, birthdate):
        """sets birthday to datetime.date format?"""
        self.birthday = birthdate
        
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """returns true if self's name is lexicographically                 less than other's name, false otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def _str_(self):
        return self.name
    
class MITPerson(Person):
    nexIdNum = 0
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nexIdNum
        MITPerson.nexIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    
class Grad(Student):
    pass

class TransferStudent(Student):
    def __init__(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool
        
    def getOldSchool(self):
        return self.fromSchool
    
    
    
    
p1 = MITPerson('Barbara Beaver')
print(str(p1.name) + '\'s id number is ' + str(p1.getIdNum()))

