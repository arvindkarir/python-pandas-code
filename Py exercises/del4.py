# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:13:48 2018

@author: User
"""
filepath = 'A10_01_data.txt'
with open(filepath) as afile:
    afile = open(filepath, 'r')
    while True :
        line = afile.readline()
        print(line)
        if ("" == line):
            print ("file finished")
            break;

#
#    line = afile.read() # this is taking the first line and doing nothing with it
#    oneval, twoval, threeval, fourval = [],[],[],[]
#    if line == '':
#        filepath.close()
#    else:
#        print(line.split('\n')[0])