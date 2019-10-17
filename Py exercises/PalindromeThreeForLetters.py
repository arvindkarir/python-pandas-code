def reverse(text):
  _letters = ''
  UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  LCLetters = 'abcdefghijklmnopqrstuvwxyz'
  #_letters = UCLetters + LCLetters
  word = ''
  for c in text:
    if c in (UCLetters + LCLetters): #_letters
      word = word + c
  print('word is', word)
  
  revText = word[::-1]
  print("reverse of input...", revText)
  return

def is_palindrome(text):
  return text == reverse(text)

something = input("Enter text: ")
if is_palindrome(something):
  print("Yes, it is a palindrome")
else:
  print("No, it is not a palindrome")
