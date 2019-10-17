# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:10:57 2018

@author: User
"""

def pwdcheck(p):
    alphaset = []
    points = countspl = 0
    strength = ''
    for i in range(ord('a'), ord('z')+1):
        alphaset.append(chr(i))
    for i in range(ord('A'), ord('Z')+1):
        alphaset.append(chr(i))
    numberset = ['1','2','3','4','5','6','7','8','9','0']
    specialset = ['!','@','#','$','%','^','&','*','(',')',' ','-']
    first = second = False
    for each in p:
        if each in alphaset:
            first = True
        if each  in numberset:
            second = True
    if first == True and second == True:
            pass # a helper function can be introduced here
    else:
#        print('pwd not valid')
        print( 'False,', '("'+(p)+'")','failed basic test')
        return
    for each in p:
        if each in specialset:
            countspl +=1
    points = (countspl-1)*10
    if len(p) < 5:
        points -= 10
    if len(p) > 8:
        points += 15
    if points < 25:
        strength = 'weak'
    if  25 < points < 40:
        strength = 'medium'
    if points > 40:
        strength = 'strong'

    pointstring = "{0}:{1}".format(points,strength)
    print(pointstring)


pwdcheck('Xy 37 1-0')
pwdcheck('Yt3)(*&a%')
pwdcheck('PaSsWoRd')
