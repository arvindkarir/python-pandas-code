# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:49:26 2018

@author: User
"""
class Book:
    '''Fields: book_name (Str), author (Str), ISBN (Str), quantity (Int)'''
    def __init__(self, book_name, author, ISBN, no_off):
        self.book_name = book_name
        self.author = author
        self.ISBN = ISBN
        self.no_off = no_off
        print('Book record for ISBN %s created' % self.ISBN )

    def description(self):
        desc_str = "%s, %s, %s, %s" %(self.book_name, self.author, self.ISBN, self.no_off)
        return desc_str

    def quantity(self):
        print('There are %s books in stock of %s' %(self.no_off, self.book_name))
        return self.no_off

    def add_to(self, addition_qty):
        self.no_off = self.no_off + addition_qty
        print('Increased stock of %s to %s' %(self.book_name, self.no_off))
        return self.no_off

    def reduce_from(self, reduced_qty):
        self.no_off = self.no_off - reduced_qty
        print('Decreased stock of %s to %s' %(self.book_name, self.no_off))
        return self.no_off

    def delete_record(rem_book_name):
        for each in inventory:
            if each.book_name == rem_book_name:
#            print(each.description())
                inventory.remove(each)
                print('%s was removed, %s books in stock discarded' %(each.book_name, each.no_off) )
        for items in inventory:
            print(items.description())

    def check_reorder():
        for each in inventory:
            if each.no_off < 10:
                print('%s needs to be re-ordered' %each.book_name)

#bookone = Book('Harry Potter And The Order Of The Phoenix', 'JK Rowling', '0747551006', 50)
#booktwo = Book('Harry Potter And The Prisoner Of Azkaban', 'JK Rowling','1856136175', 30)

inventory = [Book('Harry Potter And The Order Of The Phoenix', 'JK Rowling', '0747551006', 50), Book('Harry Potter And The Prisoner Of Azkaban', 'JK Rowling','1856136175', 30)]
inventory += [Book('another book', 'by me', '000999', 29)]
inventory += [Book('Eric Carle', 'by Eric', '0000', 0)]

inventory[1].quantity()
(inventory[0].add_to(10))
(inventory[1].reduce_from(28))
print(inventory[1].description())
Book.delete_record('Harry Potter And The Order Of The Phoenix')
Book.check_reorder()
