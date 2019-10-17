# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:42:48 2018
for group by in dictionaries
https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch01s15.html
with itertools

@author: User
"""
# this is to get Names and courses in a list of lists:
#def getNames():
#    nameFile = open('names.txt', 'r')
#    readFile = nameFile.readlines()
#    Types = [line.split("\n") for line in readFile]
##    print(Types)
#    nameList = [Type[0] for Type in Types]
##    print(nameList)
#    listOfNames = []
#    for aName in nameList:
#        listOfNames.append(aName.split( '\n'))
#    return listOfNames
#
#print(getNames())

#
#def aDictMethod(dict1):
#    revDict = {}
#    for k, v in dict1.items():
#        if v not in revDict:
#            revDict[v] = set()
#        revDict[v].add(k)
#    return revDict
#
#dict1 = {
#'CS115' : 'Alice Dean',
#'MATH135' : 'Alice Dean',
#'MATH200' : 'Alice Dean',
#
#print(aDictMethod(dict1))


#work in progress
#def getNames():
##    newDict = {}
#    nameFile = open('names.txt', 'r')
#    readFile = nameFile.read()
#    nameFile.close()
##    print(readFile)
#    for block in readFile.split('\n\n'):
#        for line in block.splitlines():
#            print(line)
##            person[k] = v
##            print(k, v)


#
#    for line in readFile:
#        if not line.strip():
#            (key, value) = line.split("\n")
#            newDict[key] = value
#        print(newDict)

def getNames():
    aDict = {}
    readFile = open('names.txt', 'r')
    nameFile = readFile.readlines()
    readFile.close()
    outFile = []
    for i in range(len(nameFile)):
        if nameFile[i] != '\n':
            outFile.append(nameFile[i].rstrip('\n'))
    print(outFile) # output with first element name, alternate element list of courses
#    keys = outFile[1::2]
#    values = (outFile[::2])
#    listFile = (list(zip(values, keys)))
#    personalCourseList = []
#    for item in listFile:
#        personalCourse = ''.join(str(e) for e in item[1])
#        personalCourse = personalCourse.split()
#        personalCourseList.append(personalCourse)
#    personalFile = list(zip(values, personalCourseList))
#    print(personalFile)

# create a set of unique course values
#    courses = ' '.join(str(e) for e in keys) #converts courses into  courses string delimited by spaces
#    courses = courses.split() # converts each course to a string value
#    courses = set(courses) # removes duplicates
##    print('unique courses are:', courses)


#    for values in readFile:
#        if values != '/n/n':
#            values = values.split()
#            print(values)
#        key = next(readFile, None)
#        my_dict[key.strip()] = values
#    print(my_dict)



(getNames())