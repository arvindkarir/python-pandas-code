# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:31:36 2018

@author: User
"""
# part 1-e
def multlist(m1, m2):
    lenof = len(m1)
    newl = []
    for i in range(lenof):
        newl.append( m1[i]* m2[i])
    print(None)

m1=[1, 2, 23, 104]
m2=[-3, 2, 0, 6]
multlist(m1, m2)

# part 1-a
#def createodds(n):
#    lofodds = []
#    for i in range(1,n, 2):
#        lofodds.append(i)
#    print(lofodds)
#createodds(0)

# part 1-b
#def spllist(n):
#    newlist = []
#    for i in range(1,n):
#        smallist = list(range(1,i))
#        newlist += [smallist]
#    print(newlist[1:])
#spllist(6)

# part 1-c
#def divisibles(n):
#    lol = []
#    for i in range(1, int(n/2)+1):
##        print(i)
#        if n%i == 0:
#            lol.append(i)
#    print(lol)
#
#divisibles(19)

# part 1-d
#def update(l, a, b):
#    count = 0
#    newl = l
#    for i in range(len(l )):
##        print(l[i])
#        if l[i] == a:
#            newl[i] = b
#            count += 1
#    s = ('newlist is {0}, and {1} was replaced {2} times')
#    print(s.format(newl, a, count))
#
#nl = [3, 10, 5, 10, -4]
#update(nl, 10, 7)


#def afn(los): # join various elements of a list recursively
#    news = los[0:]
#    if los == []:
#        return
#    else:
##        print(los[1:])
#        news = news + [afn(los[1:])]
#    print(news)
#
#s = ['abc', 12, True, '',-12.4]
#print(afn(s))
