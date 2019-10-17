def bisect(lst, n):
  lst = sorted(lst) #need to sort it, otherwise error, comment it out and see
  high = len(lst) #the max value. Don't go minus 1 as rounding off will cause
                  #last value to be ignored
  low = 0
  mid = (high + low)//2  #a starting mid
  while high > low and high != mid and low != mid: #before reaching the middle
    print('hi, low, mid:', high, low, mid)
    if n > lst[mid]: #compare to mid'th value in lst
      low = mid #as it is high, move to right of mid
      mid = (mid + high)//2 #new mid is to the right of scale
    elif n < lst[mid]: #if low, then to left of scale
      high = mid
      mid = (low + mid)//2
    else:
      return mid
  print('element not found')
  
lst = [44,55,33,1,2,3,4,5,6,7,15,2,55,77,81,3,2]
print(bisect(lst, 81))
