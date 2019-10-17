# this works and evaluates even numbers, prints 'no even numbers' in case thereof...
def checkEven(lst):
  global evenNos  # global defines this variable outside of the function
  evenNos = []  #start with empty list
  for i in lst:
    if i%2 == 0:
      evenNos.append(i) #create a list of even numbers

lst = [1,3,33,2,66,88,55,77,33,55,5,7]
while True:
  checkEven(lst)
  try:
    val = 1/len(evenNos)
    print 'list of even numbers:', evenNos
    print 'first even number:', evenNos[0]
  except ZeroDivisionError:
    print 'no even number'
  break  
