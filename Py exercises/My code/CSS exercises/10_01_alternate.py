# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:02:01 2018

@author: User
"""

def get_stats(filename):
    f = open(filename, 'r')
    raw_data = f.readlines()
    f.close()
    data_length = (len(raw_data))
    try:
        process_data(raw_data)
    except:
        if data_length == 0:
            print('file too small')

def process_data(raw_data):
    data_list = []
#    print(raw_data)
    for each in raw_data:
        data_list.append(each.strip('\n'))
    just_data =(data_list[1:])
    value_1 = value_4 = 0
    value_2 = value_3 = []
    for each in just_data:
#        print(each.split(','))
        value_1 += float(each.split(',')[0])
        value_2.append(each.split(',')[1])
        value_3.append(each.split(',')[2])
        value_4 += float(each.split(',')[3])
    print(value_1/4, min(value_2), max(value_3), value_4 )


get_stats('A10_01_data.txt')