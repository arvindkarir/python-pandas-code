# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:03:46 2017
various recursion examples
"""
def recurX(x, n): #multiplication by recursive addition
    if n ==1:
        return x
    else:
        return x + recurX(x, n-1)
#print(recurX(28,500))
# -----------------------------
#add items in a list by recursion: -->
def sumList(items):
    if len(items) ==1:
        return items[0]
    else:
        return items[0] + sumList(items[1:])
    
#print(sumList([2, 4, 5, 6, 7]))
# ------------------------------
# program to convert an integer to a string in any base
def toBase(n, base):
    pickValue = "0123456789ABCDEF"
    if n < base:
        return pickValue[n] #pick the nth value
    else:
        return toBase(n//base,base) + pickValue[n % base]

#print(toBase(24,2)) #here 24 to base 2 = 11000
#print(toBase(512,3)) #200222
# ------------------------------
# recursive sum of elements in a list including list of list
# or a summing of nested list
def total_of_list(dataList):
    totalist = 0
    for element in dataList:
        if type(element) == type([]):
            totalist = totalist + total_of_list(element)
        else:
            totalist = totalist + element        
    return totalist
            
#print(total_of_list([1,2,[3,4],[5,6]]))

# another solution to summing of nested list is: 
def sumofLists(NL):
    if isinstance(NL, int):
        return NL
    sum = 0
    for i in range(0, len(NL)):
        sum = sum + sumofLists(NL[i])
    return sum
print(sumofLists([1,2,[3,4],[5,6]]))

# --------------------------------
def harSum(n):
    if n < 2 :
        return 1
    else:
        return float(1/n) + harSum(n-1)
# sum of series like 1 + 1/2 + 1/3 + .... 1/n
#print(harSum(4))
# ---------------------------------

def fastFib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) +fastFib(n-2, memo)
        memo[n] = result
        return result

# print(fastFib(120)) #8 670 007 398 507 948 658 051 921, eight trillion trillion something!
        
# --------------------------------
# following is a countup recursion program
def countup(n):
    if n >= 0: 
        countup(n - 1) #the loop keeps on going to n-1 and storing n's from top down to 1
        print(n) # since the print is outside, the n values are printed as the function unravels from inside out, and n value counts up
# check https://cscircles.cemc.uwaterloo.ca/16-recursion/ for visualization of the loop
        
#print('Blastoff!') #this line is printed first
#countup(5) # this line executed next

# ---------------------------------
# Nov 23-2017 this exercise was revealing in recursiveness of functions and how return is calculated. I dreamt of recursions that night - BAD!

def digitalSum(n):
    if n < 10:
      return n
    else:
      return n%10 + digitalSum(n//10)
  
# print(digitalSum(1234331))
      
# ----------------------------------
# hailstone with while loop
def hailstone(n):
    if n == 0 or n ==1:
        print('1')
           
    while n >1:
        if n%2 == 0:
            print(n)
            hailstone(n//2)
        else:
            print(n)
            hailstone(3*n + 1)
        break
# print(hailstone(4))
# -----------------------
# another hailstone solution without while loop, the only issue, it returns none at the end of sequence
def hailstone_2(n):
    if n == 0 or n ==1:
        print('1')
    elif n%2 == 0:
        print(n)
        hailstone_2(n//2)
    else:
        print(n)
        hailstone_2(3*n + 1)
 
hailstone_2(5)

# -----------------------------
# find a value in a nested list
# cannot get it to print False

def isThere(NL, val):
    if isinstance(NL, int):
        return NL 
    for i in range(0, len(NL)):
        if val == NL[i]:
            print(True)
        else:
            isThere((NL[i]), val)

NL =   [8, 2, [3,4],[9,9,[0]], [5,6]]          
isThere(NL, 87)
        
        


