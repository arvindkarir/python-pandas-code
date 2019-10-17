# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:33:55 2018

@author: User
"""

def word_count(para):
    word_dict = {}
    location_list = []
    ''' This code was just the beginning to generate dict and count
    words = {}
    for sentence in para:
        for word in sentence.split(' '):
            word = word.strip('.')
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    #    for key, values in words.items():'''
    for j in range(len(para)):
        sentence = para[j].split(' ')
        for i in range(len(sentence)):
            sentence[i] = sentence[i].strip('.').strip(',')
            location_list += [ [sentence[i], [ j+1, i+1]] ]
#    print(location_list)
    for i in range(len(location_list)) :
#        print(location_list[i][0], location_list[i][1])
        if location_list[i][0] in word_dict:
            word_dict[location_list[i][0]] += [location_list[i][1]]
        else:
            word_dict[location_list[i][0]] = [location_list[i][1]]
    print(list(word_dict.items()) )


s = ['CS116 is difficult.', 'However, CS116 is also full of fun.']
word_count(s)