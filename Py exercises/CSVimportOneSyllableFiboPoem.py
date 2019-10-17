#A Fibonacci poem from a list of single syllable words
#first line = one word, second one, three, five and so on

import csv #csv import function
with open('singlesyllable.csv') as csvfile:   #file sitting in same directory
    readCSV = csv.reader(csvfile, delimiter=',')
    syllables = []    #empty list
    for row in readCSV:
        syl_1 = (row[0]) #somehow this reads as column 1
        syllables.append(syl_1) #adding to the list, or syllables.append(row[0])
syllables_set = set(syllables)  #converting to a set, no duplicates
print(syllables_set)

#these lines for testing
set_long = len(syllables_set)   #testing code
print (set_long)
set_long = set_long + 1
import random   #don't forget this line for main function below
ran_1 = random.randint(0, set_long)
ran_2 = random.randint(0, set_long)

print(ran_1)    #test
print(ran_2)    #test

a,b = 0,1
while b < 20:
    print(random.sample(syllables_set, a))  #The 'poem'!!
    a, b = b, a+b
# Need to figure out how to add this to lines (append?)

