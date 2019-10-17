#Palindrome check for string s
#Oct 31-2017 does not take and evaluate inputs
#also does not run the functions in testpal...

def palCheck():
    s = str(input('Enter word for check\n'))
    def toChars(s):
        s = [element.lower() for element in s] #convert each element to lowercase
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    
def isPal(s):
        print(' isPal called with', s )    #printing the string
        if len(s) <= 1: #zero or one letter case
            print('Base case is always true') 
            return True
        else:
            ans = s[0] == s[-1] and isPal(s[1:-1]) #isPal called inside, recursive function
            print('Return', ans, 'for', s)
            return ans

def testpal():
    print('Try dogGod')
    print('palCheck(dogGod)')
