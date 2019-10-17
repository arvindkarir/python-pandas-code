def fib(n):  # write Fibonacci series up to n
  a,b = 0,1
  while b < n:
    a, b = b, a+b
    print(b)
    
def fib2(n):  # return Fibonacci series up to n
    result =[]
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        result.append(b)
    return result

def testFib(n):
        for i in range(n+1):
                print 'fib of', i, '=', fib(i)
