'''Extract numbers from a string and provide their total'''

def sumDigits(s):
  digits = '0123456789' # define the digits
  sum = '' # initialize sum
  for pos in s: #for each position in string s
    if pos in digits:   #evaluate each item
      sum = sum + pos   #makes a string of numbers

  if sum:
    print sum
    print 'no of digits', len(sum) #this is still a STRING!!
  else:
    print 'no numbers found'
  

  total = 0    #initialize variable
  newi = 0     #initialize
  for i in sum[:]:    #now iterate over each position in string 'sum'
      print i
      newi = int(i)   #define each element as an integer
      total = newi + total    #start adding
  print total         #prints sub total and final total

