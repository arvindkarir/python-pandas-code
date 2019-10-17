# to find divisors for n numbers, returns a tuple containing all common divisors
# works on repl.it but not in Python shell!!
def fi(): #to run this function type fi() on command prompt
  n1 = input('n1=')
  n2 = input('n2=')
  n3 = input('n3=')

  divisors = () #the empty tuple
  for i in range(1, min (n1, n2, n3) + 1):
    if n1%i == 0 and n2%i == 0 and n3%i == 0:
     divisors = divisors + (i,)
    
  print (divisors)
  total = 0
  for d in divisors:
    total += d
  print (total)
