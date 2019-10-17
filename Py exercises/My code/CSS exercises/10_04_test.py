# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 12:26:06 2018

@author: User
"""
#
#def processinfo(s):
#    fields = s.split(",")
#    data = Loan( fields[0].strip("[(") , fields[1], fields[2], float( fields[3].strip( ")]" ) ) )
#    return data
#
#def getdata(inputfilename):
#    loanfile = open(inputfilename, 'r')
#    loans = map(processinfo, loanfile.readlines())
#    loanfile.close()
#    print(list(loans) )
#
#
#getdata("testingfile.txt")

from testingfile import my_list
for item in my_list:
    print(item)