EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
'eat':'mange', 'drink':'bois', 'John':'Jean',
'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
'mange':'eat', 'bois':'drink', 'Jean':'John',
'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}


def translateWord(word, dictionary):
  if word in dictionary.keys():
    return dictionary[word]
  elif word != '':
    return '"' + word + '"'
  return word


def translate(phrase, dicts, direction):
  UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  LCLetters = 'abcdefghijklmnopqrstuvwxyz'
  letters = UCLetters + LCLetters
  dictionary = dicts[direction]
  translation = ''
  word = ''
  for c in phrase: #for each and every letter
    if c in letters:
      word = word + c
      print 'word is,' , word #making a word using space or comma or such dileanators, somehow it understands and keeps the commas from original to translation
    else:
      translation = translation + translateWord(word, dictionary) + c
      print 'translation is', translation #translated string so far
      word = '' # resetting the word to empty, moving on to next
  return translation + ' ' + translateWord(word, dictionary)
  
  # type at prompt=> translate('I,drink,good,red,wine,and eat bread', dicts,'English to French')
  # => translate('Je bois du vin rouge.', dicts, 'French to English')
