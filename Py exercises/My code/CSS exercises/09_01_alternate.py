# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:55:16 2018

@author: User
"""
def by_courses(file):
    lol = []
    name_dict = {}
    f = open(file, 'r')
    all_details = f.read()
    lol.append([all_details])
    f.close()
    all_details = [line for line in all_details.split('\n') if line.strip() != ''] # strip the lines of newline and blank line
    for each in all_details:
        each = ((each.split(' ')))
        name = each[0] + ' ' + each[1]
        courses = (each[2::])
        courses = un_camel(courses)
        courses = [item for item in courses.split(' ')] # split into courses
        courses = [x for x in courses if x!= ''] # remove empty
        name_dict[name] = (courses)
    for k, v in name_dict.items():
        print(k,'-->', v)
    all_courses = (list(name_dict.values()))
    courses_set = []
    for each in all_courses:
        for item in each:
            if item in courses_set:
                pass
            else:
                courses_set.append(item)
    revDict(name_dict, courses_set)


def revDict(name_dict, alist):
    d1 = {k: [] for k in alist} # initialize an empty dictionary for all the courses
    for k, v in name_dict.items():
        for i in v:
            if i in alist: # if the course name in alist
                d1[i].append(k) # append the name
    for k,v in d1.items():
        print([k, sorted(v)])

def un_camel(courses): # convert from camelcase to uppercase
    uc_text = ''
    for x in courses:
        for item in x:
            if item.islower():
                uc_text += item.upper()
            else:
                uc_text += item
        uc_text += ' ' # to add blank spaces between courses
    return uc_text

by_courses('Names.txt')

#    b = {y:x for x,y in name_dict.items()} # just an experiment to see dictionary reversal - doesn't help in this case tho
#    print(b.items())












