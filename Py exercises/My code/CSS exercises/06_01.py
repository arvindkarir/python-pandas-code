# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 12:35:33 2017

@author: User
"""

def bookRecord(n):
    lolBooks = []
    lstBook = []
    for i in range (n):
        name = input('book name')
        author = input('author')
        ISBN = input('ISBN')
        qty = int(input('qty'))
        lstBook = ['name'+ 'author'+ 'ISBN'+'qty']
    lolBooks.append(lstBook)
    return lolBooks

print(bookRecord(2))
