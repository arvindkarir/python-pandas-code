#to identify any common words in two strings using sets
def str_comp(x, y):
  x = str(raw_input('Enter first string\n'))
  y = str(raw_input('Enter second string?\n'))
  print 'You entered\n', x, ',', y
  s1 = set(x.split())
  s2 = set(y.split())
  list_dup = s1.intersection(s2)
  
  print 'duplicates are', list_dup    
