x = 123454321
epsilon = 0.001 #precision
numGuesses = 0
low = 0.0
high = max(1.0, x) #any number can be used as long as >1.0
ans = (high + low)/2.0 #just a starting point in middle
while abs(ans**2 - x) >= epsilon: #as long as we have not reached epsilon
  print 'low =', low, 'high =', high, 'ans =', ans
  numGuesses += 01 #step increment of 1
  if ans**2 < x:
    low = ans  #low needs to go up
  else:
    high = ans #high needs to come down
  ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x
