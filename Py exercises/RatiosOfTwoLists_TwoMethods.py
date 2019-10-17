#ratios of two equal length lists using try and except commands

def getRatios(vect1, vect2):
  ratios = []
  if len(vect1) != len(vect2):  #compare two vectors
    print len(vect1), 'is not equal to', len(vect2)
    print 'vectors not equal, not evaluating'
    return
  else:
    for index in range(len(vect1)): #cycling thru elements
      try:
        ratios.append(vect1[index]/float(vect2[index]))   #evaluating
      except ZeroDivisionError:
        ratios.append(float('nan')) #if division by zero
  return ratios
  
print getRatios([2.0, 3.0,2.0], [1.2,0.0, 2.0])


# Another longer implementation
#ratios of two equal length lists - longer code

def getRatios(vect1, vect2):
  ratios = []
  if len(vect1) != len(vect2):
    raise ValueError('getRatios called with bad arguments')
  for index in range(len(vect1)):
    vect1Elem = vect1[index]
    vect2Elem = vect2[index]
    if (type(vect1Elem) not in (int, float)) or (type(vect2Elem) not in (int, float)):
      raise ValueError('getRatios called with bad arguments')
    if vect2Elem == 0.0:
      ratios.append(float('NaN'))   #NaN is not a number
    else:
      ratios.append(vect1Elem/vect2Elem)
  return ratios
  
 
try:
  print getRatios([1.0,2.0,7.0,6.0], [1.0,2.0,0.0,3.0])
  print getRatios([], [])
  print getRatios([1.0, 2.0], [3.0])
except ValueError, msg:
  print msg
