# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:26:55 2017

@author: User
"""
#listBooks = [[34587,'Learning Python', 'Mark Lutz',4, 4095],[98762,'Programming Python', 'Mark Lutz',5, 5680],[77226,'Head First Python', 'Paul Barry',3, 3295],[88112,'Einführung in Python3', 'Bernd Klein',3, 2499]]
#
#def listOfLists():
#    lst = map(lambda s: (s[0], s[3]*s[4]/100), listBooks)
#    return list(map(lambda y: (y[0], y[1]+10) if y[1] < 100 else y, lst))
#
#print(listOfLists())


#list2Books = [34587,['Learning Python', 'Mark Lutz',4, 4095],['Programming Python', 'Mark Lutz',5, 5680],['Head First Python', 'Paul Barry',3, 3295],['Einführung in Python3', 'Bernd Klein',3, 2499]]
#
#def list2OfLists():
#    subList = list2Books[1:]
#    orderNo = list2Books[0]
#    return list(map(lambda s: (orderNo, (s[3]*s[2]/100)) , subList))
#
#print(list2OfLists())
#

list3 = [ [1, ("5464",4,9.99), ("8274",18,12.99), ("9744",9,44.95)],[2, ("5464",9,9.99), ("9744",9,44.95)],[3, ("5464",9,9.99), ("88112",11,24.99)],[4, ("8732",7, 11.99), ("7733",11,18.99), ("88112",5,39.95)] ]
from functools import reduce
def list3oflists():
    invoiceTotal = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), list3))
    totalbyOrder = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], invoiceTotal))
    print(invoiceTotal, totalbyOrder)

print(list3oflists())