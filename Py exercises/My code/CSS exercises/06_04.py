# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:41:09 2017

@author: User
"""
# kind of longer code
#def bookRecord(n):
#    lolBooks = []
#    for i in range (n):
#        lstBook = []
#        name = input('book name')
#        lstBook.append(name)
#        author = input('author')
#        lstBook.append(author)
#        ISBN = input('ISBN')
#        lstBook.append(ISBN)
#        qty = int(input('qty'))
#        lstBook.append(qty)
#        lolBooks.append(lstBook)
#        lolBooks.append([name, author, ISBN, qty])
#    return (lolBooks)

# Another version
def bookRecord(n):
    lolBooks = []
    for i in range (n):
        name = input('book name')
        author = input('author')
        ISBN = input('ISBN')
        qty = int(input('qty'))
        lolBooks.append([name, author, ISBN, qty])
    return (lolBooks)

print(bookRecord(2))

a = [['q', 'w', 'e', 0], ['a', 's', 'd', 2]]

def updateQty(lolBooks):
    ISBNno = input('ISBN number to search')
    changeQty = int(input('Item count to increase or decrease'))
    for i in range(len(lolBooks)):
        if lolBooks[i][2] == (ISBNno):
            lolBooks[i][3] += changeQty
            print('Name of book is,', lolBooks[i][0], 'updated stock is', lolBooks[i][3] )
            return
    print('Book not found')

def deleteBook(lolBooks):
    ISBNno = input('ISBN number to delete')
    for i in range(len(lolBooks)):
        if lolBooks[i][2] == (ISBNno):
            print('Record of book with ISBN number', ISBNno, 'is being deleted.')
            lolBooks.pop(i)
            print(lolBooks)
            return
    print('Book not found')

def reorderBook(lolBooks):
    for i in range(len(lolBooks)):
        if lolBooks[i][3] == 0:
            print('The following needs to be reorderd', lolBooks[i])
            return
    print('Nothing to reorder')
#
#updateQty(a)
#deleteBook(a)
reorderBook(a)

