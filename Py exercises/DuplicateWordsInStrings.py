#to identify any common words in two strings
#first_str = str('i am  not a dog and i am not an animal')
#second_str = str('i am a cat but i am a dinosaur')
def str_comp(x, y):
  x = str(raw_input('Enter first string\n'))
  y = str(raw_input('Enter second string\n'))
  print 'This is what you entered\n', x, ',', y
  list_1 = x.split()
  list_2 = y.split()
  list_dup = []
  for i in range(len(list_1)):
   for j in range(len(list_2)):
     if list_1[i] == list_2[j]:
        list_dup.append(list_2[j])
  print 'duplicates are', list_dup    
  print 'two lists are', list_1, list_2
