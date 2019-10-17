# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:29:46 2018

@author: User
"""
from collections import OrderedDict

def word_count(file_name):
	f = open(file_name, 'r', encoding="utf8")
	raw_data = f.read().lower().split()
	f.close()
	stopwords = set(line.strip() for line in open('stopwords.txt'))
	data_list = []
	word_cloud_dict = {}
	for each in raw_data:
		data_list.append(each.strip('\n').strip('' ':' ';' '"' ':' '.' ',' '-''?' '--' '-' '"'))
	for word in data_list:
		if not word in stopwords:
			if not word in word_cloud_dict:
				word_cloud_dict[word] = 1
			else:
				word_cloud_dict[word] += 1

	new_dict = OrderedDict( sorted(word_cloud_dict.items(), key = lambda t: t[1], reverse=True))
	for k,v in new_dict.items():
		if v >= 25:
			print(k, v)



word_count('Tale_of_two_cities.txt')