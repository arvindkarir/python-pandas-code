'''check input for integers, do their square. If it is a string, print string (which may be true for all cases but integers'''


def readVal(valType, requestMsg, errorMsg):
  while True:
    val = raw_input(requestMsg + ' ')
    try:
      val = valType(val) #if this tries to find valType int of a string, it generates an error, so goes to except block
      return val
    except ValueError:
      print val, errorMsg
      
      

val = readVal(int, 'Enter integer:', 'is not an integer') #this will invoke the readVal function for integers
print 'square of', val, 'is:', val**2

print 'now evaluating a string'
val = readVal(str, 'Enter a string:', 'is not a string') #this will invoke the readVal function for string
print 'just another string', val
