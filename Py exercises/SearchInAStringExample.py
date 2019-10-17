def search(L, e):
  
  def bSearch(L, e, low, high):
    if high == low:
      return L[low] == e
    mid = (low + high)//2
    print low, mid, high
    if L[mid] == e:
      return True
    elif L[mid] > e:
      if low == mid:
        print 'another loop'
        return False
      else:
        print 'another'
        return bSearch(L, e, low, mid -1)
    else:
      return bSearch(L, e, mid + 1, high)
      
  if len(L) ==0:
    return False
  else:
    return bSearch(L, e, 0, len(L) -1)
    

L = [1, 2, 7, 3, 4, 6, 5, 8]
L.sort()
T = sorted(L)
print L
print T
#print search(L, 3)
