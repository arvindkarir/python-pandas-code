# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 22:20:06 2018

@author: User
"""
def getNames():
    readFile = open('names.txt', 'r')
    nameFile = readFile.readlines()
    readFile.close()
    outFile = []
    # code below creates lines as strings with /n as spaces
    for i in range(len(nameFile)):
        if i != "\n\n":
            outFile.append(nameFile[i].rstrip('\n'))
    outFile.append('')
    oneMore = []
    # code below creates lol, with fullname, followed by list of courses
    for line in outFile:
        if line.strip(): # non empty line
            details = line.split(" ", 6)
#            print(details)
            name = []
            courses = []
            for i in range(len(details)):
                name = [details[0] +' '+ details[1]]
                courses = (details[2::])
                name.append(courses)
            oneMore += [name]
#    print(oneMore)
    d = {}
    createName(oneMore, d)
    # Now to create unique courses
    courseKeys = []
    for i in range(len(oneMore)):
        coursesets = (oneMore[i][1])
        for course in coursesets:
            if course not in courseKeys:
                courseKeys.append(course)
    print(courseKeys)
    revDict(d, courseKeys)

def revDict(d, L):
    d1 = {k: [] for k in L}
    for k, v in d.items():
        v= tuple(v)
        for i in v:
            if i in L:
                d1[i].append(k)
    for k,v in d1.items():
        print([k, sorted(v)]) # Done!!!


def createName(L, d):
    # creates name instances and course instances
    theName = []
    theCourses = []
    for i in range(len(L)):
        nameList = L[i][0].split()
        theName = str(nameList[0] + ' ' + nameList[1])
        for j in range(len(L[i][1])):
            (L[i][1][j]) = (L[i][1][j]).upper() #cannot replace left hand value by a variable, it messes it up
            theCourses.append( (L[i][1][j]) )
        d[theName] = (theCourses)
        theCourses = []
    return d

getNames()

#Arvind Karir MATH100 CS116 MATH200
#Amour 2Karir CS116 CS214 Math100 MATH200
#Anya 1Karir maTH100 PHY101 ENG101
#Avani 3Karir PHY101 ENG101 SOC211 CS116
#Alka 0Karir eng101 MATH100 CS116
# 'MATH100', 'CS116', 'MATH200', 'CS214', 'PHY101', 'ENG101', 'SOC211'




























