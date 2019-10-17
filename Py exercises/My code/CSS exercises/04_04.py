# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:12:02 2017

@author: User
"""
#import re
#from future import print_function
#from itertools import islice
#from operator import itemgetter

keyDict =  {' ': '0', '.':'1', ',':'1', '?':'1','a': '2', 'b': '2', 'c': '2','d': '3', 'e': '3', 'f': '3','g': '4', 'h': '4', 'i': '4','j': '5', 'k': '5', 'l': '5','m': '6', 'n': '6', 'o': '6','p': '7', 'q': '7', 'r': '7', 's': '7','t': '8', 'u': '8', 'v': '8','w': '9', 'x': '9', 'y': '9', 'z': '9'}
# THIS IS COMPLETE CODE INCLUDING TEST FUNCTIONS
#########################################################
#keyDict = {1:'a',2:'b',3:'cc',4:'rt', 5:'a'} # Smaller test set
# Separating Digits from keyPresses
#----------------------------
keyCode = [[6,3], [0,1],[5,2]] # initial keys, digit and presses
keyCode = (sum(keyCode, [])) # flatten the list
#print(keyCode) # check
# Instead of enumerate, use map and lambda


# check functions......
#print(keyDigit) # check
#print(keyPresses) # check
#
#def afn(x): # just a function to print cycling thru
#    print(x)
#
#list(map(lambda x: afn(x), keyPresses)) #cycling working
#----------------------------
# Getting values specific to a key
# Working with one key for now
aKey = '6' # works for 0, 1 etc..
keyS = []

def bfn(k): # function to get all the values to a keyDigit
    if aKey in k:
        keyS.append(list(k)) # very important line, if list is missing then I get a bunch of tuples inside a list, which cannot be flattened
list(map(lambda k: bfn(k), keyDict.items())) #cycling working, yay!!
#print('keyS as dict list', keyS)
keyS = (sum(keyS, [])) # flatten the list of lists to a list
#print('oldkeys, flat list:', keyS)
#keyS = (list(filter(str.isalpha , keyS))) # removed the numbers. BUT this is not good as the space gives '0' which can be stripped
# Alternative
keyS = keyS[::2]# extract even index values
#print('newkeys=', keyS) # check

# Test function
# ---------------------
#def cfn(i):
#    print (i)
#
#list(map(lambda i: cfn(i), keyS))
# -----------------------------

# Getting letter corresponding to keyPresses
#print('keyS', keyS)
#print('keyPresses', keyPresses)
indexVal = keyPresses[0]
#print(indexVal)
#print(keyS.index('m'))
print(keyS[indexVal-1])


####################
# another version that did not work
#
#keyCode = [[6,3], [0,1],[5,2]] # initial keys, digit and presses
#keyCode = (sum(keyCode, [])) # flatten the list
## Use map and lambda to extract even and odd values
#keyDigit = list(map(lambda i: keyCode[i],filter(lambda i: i%2 == 0,range(len(keyCode)))))
#keyPresses = list(map(lambda i: keyCode[i],filter(lambda i: i%2 == 1,range(len(keyCode)))))
## Check function
#print(keyDigit)
#print(keyPresses)
#
#valueDict = list(keyDict.values())
#keysDict = list(keyDict.keys())
#print(valueDict, keysDict)
#keyS = []
#
#def bfn(x): # function to get all the values to a keyDigit
#    for x in keyDigit:
#        if x in valueDict:
#             keyS.append(list(x)) # very important line, if list is missing then I get a bunch of tuples inside a list, which cannot be flattened
#
#
#list(map(lambda x: bfn(x), keyDict.items())) #cycling working, yay!!
#print(keyS)
#
#
#
#
#
#












































#########################################################
#########################################################
#keyDict = {1:'a',2:'b',3:'cc',4:'rt', 5:'a'}
#aKey = input('enter the key\n')
#placeKey = int(input('enter times pressed'))
#print(keyDict.get('p')) # gets the first value to key 'p' = 7
#print(list(keyDict.values())) # prints all values
#print(list(keyDict.keys())) # keys
#print(list(keyDict.items())) # item pairs
#print(list(keyDict)) # prints all the keys
#print(sorted(keyDict)) # keys in ascending order
#print(sorted(keyDict.values())) # values in ascending order
#print(sorted(keyDict, key=keyDict.__getitem__)) # prints keys in order of sorted values
#print([key for (key,value) in sorted(keyDict.items())]) # prints either keys or values
#keyList = list(keyDict.keys()) # list of keys
#print( {k:v for k,v in keyDict.items() if 'p' in k}) # prints '7' corresponding to p, but nothing after

#list(map(lambda v: keyS.append(v), (v for k,v in keyDict.items() if 'p' in k)))
#keyS = []
#for key, value in keyDict.items():
#    if aKey == value:
#        keyS.append(key)
#letterOut = keyS[placeKey-1] # gets the item out
#b = itemgetter(placeKey)(keyS) # also gets the item out

#print(list(map(lambda x: keyDict.get(x), keyDict))

#print(keyS, letterOut, b)
#allVals = list(keyDict.values()) # all the values
#allKeys = list(keyDict.keys()) # all the keys
#allIndices = list(map(lambda x: allKeys.index(x) , allKeys)) # all the indices
#def getMe( a, b):
#    return [a[i] for i in b]
#
#print(getMe(allVals, allIndices))
#print(getMe(allKeys, allIndices))
#
#def getKeys(dictionary, value):
#  return list(filter(lambda x: dictionary[x] == value, dictionary.keys()))
#getKeys(keyDict, 9)
#
#print( allKeys,allVals)

#print( list(map(lambda x: allKeys.index(x) , allKeys))) # gives all the indices [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
#print( list(map(lambda x: allVals.index(x) , allVals))) # gives all the indices taking first occurrence as default value [0, 1, 1, 1, 4, 4, 4, 7, 7, 7, 10, 10, 10, 13, 13, 13, 16, 16, 16, 19, 19, 19, 19, 23, 24, 23, 24, 24, 24]

#def findMethod(keyDict):
#    return (k for k,v in keyDict.items() if v == aKey)





#WIP
#def getKeys(keyDict):
#  return (value[1: keyDict.find('aKey')])
##


#def getTweetNumber(tweet):
#  return int(tweet[1: tweet.find(':')])
#
#def bfn(tweets, name):
#  return list(map(getTweetNumber, filter(lambda twt: name in twt, tweets)))




#Working
#print(keyDict.keys())
#print(keyDict.values())
#print(keyDict.items())


#def afn():
#    for key, value in keyDict.items():
#        print(key, value)
#
#(list(map(lambda x: afn(), keyDict)))

#print(list(map(lambda x: print(x), keyDict))) #kind of working

##filter(lambda x: print(lookFor) if x == lookFor else False, keyDict)
##lookFor = input('theValue')
#print(sth)



# something working
# list(map(print, keyDict)) # prints all keys



#dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
#
#print(list(map(lambda x : x['name'] == 'python', dict_a)))

# not working
# sth = re.search(r('0'), keyDict)#
#a = [{1: 'a'},{ 2: 'b'}]
#for k,v in a.items():
#    print(k, v)