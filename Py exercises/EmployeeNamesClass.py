# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:15:49 2017

@author: User
"""


class EmpNames(object):
    
    def __init__(self):
        self.vals = []
        
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
            
    def member(self, e):
        return e in self.vals
#        if e in self.vals:
#            return True
#        else:
#            return False
        
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + 'not found')
            
    def getMembers(self):
        return self.vals[:]
    
    def __str__(self): #used in invoking data in object
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'
        

partTime = EmpNames()
fullTime = EmpNames()
partTime.insert('jack')
partTime.insert('john')
partTime.insert('alan')
print(partTime)
print(partTime.getMembers())
fullTime.insert('mary')
fullTime.insert('abby')
fullTime.insert('cheri')
print(fullTime)
print(fullTime.getMembers())