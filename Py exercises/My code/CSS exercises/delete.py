# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:37:51 2018

@author: User
"""

def graph(src, dest):
    paths = {}
    paths['A'] = ['A', 'B', 'C','D', 'E', 'F', 'G']
    paths['B'] = ['B', 'D', 'F', 'G']
    for key, value in paths.items():
        if src in key:
            if dest in value:
                print('link')
            else:
                print('no link')

graph('A','C')
graph('B', 'A')