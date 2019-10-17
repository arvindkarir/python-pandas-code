def removeDups(L1, L2):
#Assumes that L1 and L2 are lists.
#Removes any element from L1 that also occurs in L2"""
  for e1 in L1[:]:
    print 'e1=', e1
    if e1 in L2:
      L1.remove(e1)

L1 = [1,2,3,4,0,8,5,9,4,3]
L2 = [1,2,5,6]
removeDups(L1, L2)
print 'L1 =', sorted(L1)

