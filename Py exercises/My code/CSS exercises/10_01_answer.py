# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:13:48 2018

@author: User
"""

def getData(readfile):
    try:
        filepath = 'A10_01_data.txt'
        with open(filepath) as afile:
            while True :
                line = afile.readline()
#                print(line)
                readfile.append(line.split(','))
                if ("" == line):
#                    print ("file finished")
                    break;
        return readfile
    except FileNotFoundError:
        print('[]')


def processInfo():
    readfile = []
    getData(readfile)
    readfile = readfile[1:]
    readfile = readfile[:-1]
    oneval, twoval, threeval, fourval = [],[],[],[]
    for each in readfile:
        oneval.append(each[0])
        twoval.append(each[1])
        threeval.append(each[2])
        fourval.append(each[3].strip('\n'))

    print(((oneval), ( twoval), (threeval), ( fourval)))
    lenof = (len(list(oneval))) #something weird happens if this lenght is defined for newone
    newone = (round(float(i),5) for i in oneval)
    newtwo = (round(float(i),5) for i in twoval)
    newthree = (round(float(i),5) for i in threeval)
    newfour = (round(float(i),5) for i in fourval)

    print( [ sum(list(newone))/lenof, min(list(newtwo)), max(list(newthree)), sum(list(newfour))] )


processInfo()