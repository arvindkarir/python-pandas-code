# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:32:28 2018

@author: User
"""

def words_num(s):
    words_in_sentence = []
    para = s.split('.')
    for sentence in para:
        if sentence == '':
            pass
        else:
            count_of_words = 0
#            print(sentence)
            for word in sentence.split(' '):
#                print(word)
                if word == '':
                    pass
                else:
                    count_of_words += 1
            words_in_sentence.append(count_of_words)
    print(words_in_sentence)

words_num('Each sentence is formed by words separated by spaces. Multiple spaces are allowed between two words.')
words_num('Each sentence is formed by words separated by spaces.')