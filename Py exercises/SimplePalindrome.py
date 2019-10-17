#palindrome
a=raw_input("enter the word")
a = a.lower()
b=a[::-1]
if a==b:
 print("entered word is palindrome")
else:
 print("not a palindrome")
