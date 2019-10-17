# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:01:37 2018
Character count using dictionary
@author: User
"""

def character_count (sentence):
  characters = {}
  for char in sentence:
    if char in characters:
      characters[char] = characters[char] + 1
    else:
      characters[char] = 1
  return characters

def most_common_character (sentence):
    chars = character_count(sentence)
    most_common = ""
    max_times = 0
    for curr_char in chars:
        if chars[curr_char] > max_times:
            most_common = curr_char
            max_times = chars[curr_char]
    return most_common

testline = ("just a test       ")
# repr helps in case the value is a space by putting quotation marks around the output value

print('the winner is:', repr(most_common_character(testline)))