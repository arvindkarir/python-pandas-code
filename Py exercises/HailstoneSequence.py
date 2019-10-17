# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:07:01 2017

@author: User
"""
import pylab


def hailstone_seq(n):
    seq = [n]
    if n < 1:
       return []
    while n > 1:
       if n % 2 == 0:
         n = n / 2
       else:
         n = 3 * n + 1 
       seq.append(n)
       print(seq)
       pylab.plot(seq, linewidth = 1)
#       figname =  "%i.png" % n
       pylab.savefig('197')
 

print(hailstone_seq(197))


    
    #hlist = hailstone_seq(55)
#
#pylab.figure(1)
#pylab.plot([1,2,3,4], [1,7,3,5])
#pylab.show()


#
#for i in range(hlist):
##    values.append(principal)
##    principal += principal*interestRate
#    pylab.title('Hailstone values')
#    pylab.xlabel('Years of Compounding')
#    pylab.ylabel('Value of Principal ($)')
#    pylab.plot(i, linewidth = 2)