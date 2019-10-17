Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def smallOdd(x,y,z): #evaluates and returns the smallest odd number
  if x%2 != 0 and y%2 !=0 and z%2 !=0: #evaluate if any even number
    if x < y and x < z:
      small = x
    elif y<z:
      small = y
    else:
      small = z
    print(small)
  else:
    print('not evaluated, sequence contains even numbers')
    
