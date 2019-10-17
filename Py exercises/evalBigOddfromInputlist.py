def bigodd(b):
  numbers=[]
  odd_list=[]
  b=int(input('how many numbers'))
  for i in range(b):
    c=int(input())
    if c%2 == 1:
      numbers.append(c)
    
  if numbers == []:
    print 'no odd numbers'
    return
  
  return max(numbers)

  
    
