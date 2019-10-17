# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:49:20 2017
Some interesting notes...

s = "string"
s[0:3] == s[:3] == s[3:len(s)] ==s[3:5+1]
so len(s) is 6
so range of (0,len(s)) will generate values from 0 to 5, or all of the string
but...
range of 0,5) will only output first five letters

"""
#%%
#def divides(m, n):
#    if n%m == 0:
#        return True
#    else:
#        return False
#def even(n):
#    return(divides(2, n))
#def odd(n):
#    return(not divides(2, n)) # use case of not + function
#print(odd(13))
##%%
#s = "string"
#for i in range(0, len(s)):
#    print(s[i])
#for i in range(0, 5):
#    print(s[i])
#
##%%
#factors = [1,2,5,10, 20]
#print(factors[0])    # this generates a value
#print(factors[0:1])  # this generates a list
## compare this to a string
#print(s[0])          # this is 's'
#print(s[0:1])        # and this is also 's'

nested = [[2,[37]],4,['hello']]
print(nested)
print(nested[0])
print(nested[0][1][0])
nested[2][0][3] = 5 # string object cannot be changed
print(nested)