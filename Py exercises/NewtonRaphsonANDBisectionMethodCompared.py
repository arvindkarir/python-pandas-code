epsilon = 0.001
k = 100000
compare_two = 0.00001 #an epsilon for comparing the two methods, NR method is better for 0.00001 and higher precision

# Newton Raphson for square root
# Find x such that x**-sth is within epsilon compare_two
count = 0
guess = k/2.0 #starting point
while abs(guess*guess - k) >= epsilon:
  guess = guess - ((guess*guess -k)/(2*guess))
  count += 1
print 'Sq root of', k, 'is approx', guess, 'in' , count, 'guesses'
print round(guess**2,9)
if (k-guess**2) <= compare_two:
  print 'NewtonRaphson method is better'
  
# Bisection method for square root 
numGuesses = 0
low = 0.0
high = max(1.0, k) #any number can be used as long as >1.0
ans = (high + low)/2.0 #just a starting point in middle
while abs(ans**2 - k) >= epsilon: #as long as we have not reached epsilon
  # print 'low =', low, 'high =', high, 'ans =', ans --- commented out for brevity
  numGuesses += 01 #step increment of 1
  if ans**2 < k:
    low = ans  #low needs to go up
  else:
    high = ans #high needs to come down
  ans = (high + low)/2.0
#print 'numGuesses =', numGuesses
print ans, 'is close to square root of', k, 'in', numGuesses, 'guesses'
print round(ans**2,9)
if (k-ans**2) <= compare_two:
  print 'Bisection method is better'
