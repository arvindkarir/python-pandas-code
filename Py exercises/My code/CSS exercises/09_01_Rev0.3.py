# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:47:16 2018

@author: User
"""

#class Name:
#    def __init__(self, fn, ln):
#        self.first = fn
#        self.last = ln
##        print(self.first, self.last, 'has been added')
#
#    def fullName(self):
#        return "%s %s" %(self.first, self.last)
#
#class Courses:
#    def __init__(self, name):
#        self.name = name
##        print(self.name)

def getNames():
    aDict = {}
    readFile = open('names.txt', 'r')
    nameFile = readFile.readlines()
    readFile.close()
    outFile = []
    for i in range(len(nameFile)):
        if i != "\n\n":
            outFile.append(nameFile[i].rstrip('\n'))
    outFile.append('')
    finaList = []
    tossList = []
    for line in outFile:
        if line != "":
            tossList.append(line)
        else:
            finaList.append(tossList)
            tossList = [] # but the courses are all jumbled up into one string
#    print(finaList)
    value = ''
    personalCourseList = []
    for each in finaList:
        value += (each[0]) + '\n'
        personalCourse = ''.join(str(e) for e in each[1])
        personalCourse = personalCourse.split()
        personalCourseList.append(personalCourse)
    print((value))
    keys = (personalCourseList)
    print((keys))


#        keys = keys.append(each[1])
#        values = values.append((each[0]))
#    print(keys, values)

#    for item in keys:
#        personalCourse = ''.join(str(e) for e in item[1])
#        personalCourse = personalCourse.split()
#        personalCourseList.append(personalCourse)
#    personalFile = list(zip(values, personalCourseList))
#    print(personalFile)


#
## This is good for assiging keys,values and making a dict
#    print(finaList)
#    for item in finaList:
#        for i in item[1:]:
#            aDict[i] = item[0]
##    print(aDict)

getNames()