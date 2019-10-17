# D = {}
# D['a'] = 1
# D['b'] = 2
# D['c'] = 3
# for k in D.keys():
#   print(D[k])
# for k, v in D.items():
#   print(k, ':', v)
 
class intDict(object):  
  def __init__(self, numBuckets):
    self.buckets = []
    self.numBuckets = numBuckets
    for i in range(numBuckets):
      self.buckets.append([])
      # print(self.buckets)

  def addEntry(self, dictKey, dictVal):
    hashBucket = self.buckets[dictKey%self.numBuckets]
    # print(hashBucket)
    for i in range(len(hashBucket)):
      if hashBucket[i][0] == dictKey:
        hashBucket[i] =(dictKey, dictVal)
        return
    hashBucket.append((dictKey, dictVal))  
  
  def getValue(self, dictKey):
    hashBucket = self.buckets[dictKey%self.numBuckets]
    for e in hashBucket:
      if e[0] == dictKey:
        return e[1]
    return None    
  
  def __str__(self):
    result = '{'
    for b in self.buckets:
      for e in b:
        result = result + str(e[0]) + ':' + str(e[1]) + ','
    return result[:-1] + '}' #result[:-1] omits the last comma


import random #a standard library module
  
D = intDict(29)
for i in range(20):
#choose a random int between 0 and 10**5
  key = random.randint(0, 10**5)
  D.addEntry(key, i)
print('The value of the intDict is:')
print(D)
print('\n', 'The buckets are:')
for hashBucket in D.buckets:
  print(' ', hashBucket)
