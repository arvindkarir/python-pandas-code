# it generates a dictionary with keys and values, still need to figure out

import random #a standard library module

def someList(numBuckets):
  buckets = []
  dictKey = 0
  dictVal = 0
  for i in range(numBuckets):
    buckets.append([])
    #print(buckets)  
  
  for i in range(20):
    dictKey = random.randint(0, 10*2)
    dictVal = i
    #print(dictKey, dictVal)
    hashBucket = buckets[dictKey%numBuckets]
    for i in range(len(hashBucket)):
      if hashBucket[i][0] == dictKey:
        hashBucket[i] =(dictKey, dictVal)
        return
    hashBucket.append((dictKey, dictVal))
    print(hashBucket)
    
D = someList(7) #this number should always be greater than range (the data set)

