# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:30:55 2017
http://thepythonguru.com/what-is-if-__name__-__main__/
@author: User
"""

def main():

    def hello():
            print("i am from my_module.py")
     
if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
     

def outsidemainfn():
    print('call from outside')
    main()
       
        
        
#
#main()

outsidemainfn()

"""if main() is called then it will execute both outsidemainfn and somefn. BUT somefn can be called by itself as well and it executes both somefn and outsidemainfn. if however outsidemainfn() is called it just executes THAT twice"""

