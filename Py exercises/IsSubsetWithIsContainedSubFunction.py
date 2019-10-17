def isSubset(L1, L2): 
  if len(L1) > len(L2):
    return isSubset(L2,L1) #the inner loop has to be larger, outer loop smaller
                            #if not, then out of range index error
  for e1 in L1:
    print('e1', e1)
    if not Iscontained(e1, L2): #checking for not contained
      return False #since the element is not found, it is not a subset
  return True #keep checking for all and if matches, is true

def Iscontained(item, lst): #checks for item in list
  for n in lst:
    if item == n:
      return True
  return False



L2 = [0,1,2, 55]  
L1 = [0,1,2,5,2,6,4]
print(isSubset(L1,L2))
