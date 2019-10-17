#Gosh!! this code provides only the value of nth
#number in Fibonacci series, not the TOTAL!!!
#WTF!!!

def fib(x):
  """Assumes x an int >= 0
    Returns Fibonacci of x"""
  global numFibCalls
  numFibCalls += 1
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
  
  print 'total', val
  print 'calls', numFibCalls

def tfib(n):
  for i in range(n+1):
    global numFibCalls
    numFibCalls = 0
    print 'fib at', i, 'th place =', fib(i)
    print 'fib called', numFibCalls, 'times.'
