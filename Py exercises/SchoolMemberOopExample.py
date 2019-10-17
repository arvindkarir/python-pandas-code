# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 20:24:14 2017

@author: User
"""
import gc #kind of brute force implementation to list all instances of a class
# look into weak references as well


class SchoolMember:
    Population = 0
    
    @classmethod # added this to keep a count of how many members in total
    def how_many(cls):
        print('We have {:d} members.'.format(cls.Population))
                    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #print('(Initializing SchoolMember: {})'.format(self.name))
        SchoolMember.Population += 1
        
    def tell(self):
        print('Name:{} Age:{}'.format(self.name, self.age), end =" ")
        
    def __gt__(self, other): #checks for greater than between two instances and returns true or false
        return self.name > other.name
          
    def allMembers():
        for obj in gc.get_objects():
            if isinstance(obj, SchoolMember):
                print('Member', obj.name)
                                     
class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher: {}'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {}'.format(self.salary))
    
    def allTeachers():
        for obj in gc.get_objects():
            if isinstance(obj, Teacher):
                print('Teacher:', obj.name)        
        
class Student(SchoolMember):

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialized Student: {}'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {}'.format(self.marks))
        
    def allStudents():
        for obj in gc.get_objects():
            if isinstance(obj, Student):
                print('Student:', obj.name)


           
t = Teacher('first_teacher', 33, 22334)
t1 = Teacher('second_teacher', 32, 33221)
s = Student('student_1', 22, 75)
n = Student('student_2', 21, 56)
# prints a blank line
#print()
#members = ([t, s, t1, n])
#for member in members:
## Works for both Teachers and Students
#    member.tell()
#SchoolMember.how_many()
#Student.allStudents()
SchoolMember.allMembers()

print(n > s)




