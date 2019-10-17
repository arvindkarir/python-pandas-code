# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:06:52 2017

@author: User
"""
from datetime import date

def main():
    today = date.today()
    print('Today is:', today)
    print('Let me get your birthdate now:' )
    my_year = int(input('Year of birth - YYYY:'))
    if my_year > today.year:
        raise ValueError('invalid year')
    my_month = int(input('Month of birth - MM:'))
    if my_month > 12 or my_month < 1:
        raise ValueError
    my_day = int(input('Day of birth - DD:'))
    if my_day > 31 or my_day < 1:
        raise ValueError
    my_birthday = date(my_year, my_month, my_day)
    print('Your birthday is on:', my_birthday)
    daysBorn = str(abs((my_birthday - today)))
    blank = daysBorn.index(' ')
    daysBorn = int(daysBorn[:blank])
    Ageyears = round(daysBorn/365, 0)
    print(Ageyears, 'years old')
    if my_birthday < today:
        my_birthday = my_birthday.replace(year=today.year + 1)
        time_to_birthday = abs(my_birthday - today)
    
    print('Have a nice birthday in', time_to_birthday.days, 'days')
    
main()