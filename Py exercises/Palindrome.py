#Palindrome check for string s
s = ['d','o','g','G','o','d'] #need to define a string

s = [element.lower() for element in s] #convert each element to lowercase

def isPal(s):
  print(' isPal called with', s )    #printing the string
  if len(s) <= 1: #zero or one letter case
    print('Base case is always true') 
    return True
  else:
    ans = s[0] == s[-1] and isPal(s[1:-1]) #isPal called inside, recursive function
    print('Return', ans, 'for', s)
    return ans
