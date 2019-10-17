# Newton Raphson for square root
# Find x such that x**-sth is within epsilon sth_else
epsilon = 0.01 #sth_else=0.01
k = 100000
count = 0
guess = k/2.0 #starting point
while abs(guess*guess - k) >= epsilon:
  guess = guess - ((guess*guess -k)/(2*guess))
  count = count + 1.0
print 'Sq root of', k, 'is approx', guess, 'in' , count, 'times'
