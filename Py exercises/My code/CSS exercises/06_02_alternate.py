# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:55:33 2018

@author: User
"""
def drink_list(s,price):
    drink_type = [['Mocha', 'Hot Beverage'], ['Coffee', 'Hot Beverage'], ['Iced Capp', 'Cold Beverage'], ['Strawberry', 'Smoothie “Cold Beverage'] ,['Steeped Tea', 'Hot Beverage'], ['Hot Chocolate', 'Hot Beverage']]
    price_list = []
    middle_list = list(zip(s, price))
    for item in middle_list:
        item = list(item)
        for drink in drink_type:
            if item[0] == drink[0]:
                item.insert(2, drink[1])
        price_list += [item]
    print(price_list)

drink_list(['Mocha' , 'Iced Capp', 'Steeped Tea'] , [2, 2, 1])
drink_list([],[])

