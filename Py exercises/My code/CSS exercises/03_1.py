# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:09:41 2017

@author: User
"""


def sameChrs():
    commonS = []
    s1 = str(input('Enter first string\n'))
    s2 = str(input('Enter second string?\n'))
    print('This is what you entered\n', s1,'\n', s2)
    if len(s2) > len(s1):
        raise ValueError
    else:
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    commonS.append(s1[i])

    print(commonS, 'are common')



sameChrs()




# same thing using sets
#    set_one = set(first_input)
#    set_two = set(second_input)
#    intersect = set_one & set_two #or s intersection(t)
#    print(intersect, 'are common')