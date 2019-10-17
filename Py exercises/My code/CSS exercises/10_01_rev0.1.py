# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:55:37 2018

@author: User
"""
# using try except block:

try:
    filepath = 'A10_01_data.txt'
    with open(filepath) as afile:
        line = afile.readline() # this is taking the first line and doing nothing with it
        oneval, twoval, threeval, fourval = [],[],[],[]
        for a in line.split(','):
            try:
                print(line.split(',')[0])
#                oneval.append(line.split(',')[0])
#                twoval.append(line.split(',')[1])
#                threeval.append(line.split(',')[2])
#                fourval.append(line.split('\n')[3])
#                return (oneval, twoval, threeval, fourval)
            except IndexError:
                print('done')
#        while len(line) != 0:
#            line = afile.readline()
##            print(len(line))
##            for s in range(len(line.split(',') )):
###                if s == '':
###                    print('Done')
###                else:
#            oneval.append(line.split(',')[0])
#            twoval.append(line.split(',')[1])
#            threeval.append(line.split(',')[2])
#            fourval.append(line.split('\n')[3])
#            print(oneval, twoval, threeval, fourval)




#            thevals = line.strip().split(',')
#            oneval, twoval, threeval, fourval = [],[],[],[]
#            for s in thevals:
#                if s =='':
#                    print('Done')
#                else:
#                    oneval.append(thevals[0])
#                    twoval = thevals[1]
#                    threeval = thevals[2]
#                    fourval = thevals[3]
#                    print(oneval, twoval, threeval, fourval)

except FileNotFoundError:
    print('[]')
#
#
#f=open('A10_01_data.txt',"r")
#line=f.readline()
#result=[]
#for x in line:
#    result.append(x.split(' '))
#print(result)






# some list comprehension trials to convert string to floats, nogo
    #            myval = list(map(lambda x: (x.replace(",", "")), thevals))
#            myval = [float(e) if e.isdigit() else e for e in line.split(',')]
#            myval = [float(s) for s in thevals ]