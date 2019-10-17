#run on repl.it
def findDivisors(n1, n2):
#Assumes that n1 and n2 are positive ints
#Returns a tuple containing the smallest common
#divisor > 1 and the largest common divisor of n1
#and n2
  divisors = () #the empty tuple
  minVal, maxVal = None, None
  for i in range(2, min(n1, n2) + 1):
    if n1%i == 0 and n2%i == 0:
      if minVal == None or i < minVal:
        minVal = i
      if maxVal == None or i > maxVal:
        maxVal = i
  return (minVal, maxVal)
  
  
  #-------------------
  
  #typing minD, maxD = findDivisors(100,200)  on the
  #command prompt runs this function and returns the
  #values to minD and maxD (they are stored)
  #Typing minD returns 2, and maxD returns 100 in this case
