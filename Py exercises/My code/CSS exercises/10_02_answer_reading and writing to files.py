# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:17:22 2018

@author: User
"""

def getData(oldfile, newfile, minline, maxline):
    fo = open(oldfile, 'r')
    nextline = fo.readline()
    data = []
    while (nextline != ""):
        nextdata = readlines(nextline)
        data.append(nextdata)
        nextline = fo.readline()
#    print(data)
    data = data[1:]
    filtdata = list(filter(lambda x: minline<=int(x[0])<=maxline, data ) )
    filtdata.insert(0, ['ref', 'state', 'city', 'dateof', 'datein\n'])
#    print((filtdata) )
    writefiles(newfile,filtdata)


def readlines(s):
    thedata = s.split(',')
#    thedata[4] = (thedata[4].strip('\n') )
    return thedata

def writefiles(name, data):
    otherfile = open(name, "w")
    for each in data:
        otherfile.writelines(each[0] + "\t" + each[1] + "\t" + each[2] + "\t" + each[3] + "\t" + "\t" + each[4] + "\n")
    otherfile.close()


#getData("sampledata.txt", "newfile.txt", 5, 10)
getData("samplenew.txt", "newfile.txt", 5, 10)

