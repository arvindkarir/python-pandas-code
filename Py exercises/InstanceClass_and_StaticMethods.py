# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:59:16 2017

@author: User
"""
import datetime

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        
        Employee.num_of_emps += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True


now_time = datetime.datetime.now()
print(str(now_time.day))
my_day = datetime.date(2017,11,16)
print(Employee.is_workday(my_day))
        
#emp_1 = Employee('abc','def',10000)
#emp_2 = Employee('kkl','ghi',12000)
#
#emp_str_1 = 'John-Doe-30000'
#emp_str_2 = 'Jane-Daa-32000'



#new_emp_1 = Employee.from_string(emp_str_1)
#new_emp_2 = Employee.from_string(emp_str_2)
#print(new_emp_1.email)
#print(new_emp_2.email)
#
#Employee.raise_amount = 1.05
#print(Employee.raise_amount)
#



#print(Employee.raise_amount)
#print(emp_2.raise_amount)
#print(emp_1.raise_amount)
#Employee.set_raise_amt(1.06)
#print(Employee.raise_amount)
#print(emp_2.raise_amount)
#print(emp_1.raise_amount)