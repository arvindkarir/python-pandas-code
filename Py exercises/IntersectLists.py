def intersect(listone, listtwo):
  tmp = []
  for e1 in listone:
    #print('e1', e1)
    for e2 in listtwo:
      #print('e2', e2)
      if e1 == e2:
        tmp.append(e1)
        #print('e2, tmp:', e2, tmp)
        break
  result = []
    #this code to eliminate duplicates
  for e in tmp: #cycle thru the tmp list elements
    if e not in result: #look for duplicates
      result.append(e)  #if not a duplicate, then add to list
      #print('e, result:', e, result) #print the list in progress with 'e'
  return result
  
  
listone = [1,2,3,3,2,3,2, 2,3,5]
listtwo = [2, 2,3,4,5,5,5]
print(intersect(listone, listtwo))
