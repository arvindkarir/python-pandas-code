# Factorial, works!!
def fact(x):
  if x <=0:
    print 'Answer not found'
    return
  ans = 1
  while x > 1:
    ans = ans*x
    x -= 1
  return ans
  print ans
