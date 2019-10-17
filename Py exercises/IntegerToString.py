def intstr(i):
  digits = '0123456789'
  if i == 0:
    return '0'
  result = ''
  while i > 0:
    p = digits[i%10] #divides the number and leaves the last digit
    print('p', p)
    result = p + result #last digit added to string
    print(result)
    i = i//10 #number divided by 10 and rounded down, thus eliminating last digit - already covered above
    print(i)
  return result
  
lst = 3344556677 #this is read as a value comprised of integers
print(intstr(lst))
