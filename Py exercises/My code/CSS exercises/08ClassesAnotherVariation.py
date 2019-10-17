# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:05:12 2018

@author: User
"""

class Airlines():

    allAir = []

    def __init__(self, code, date, fare):
        self.code = code
        self.date = date
        self.fare = fare
#        self.allAir.append(code)
#        self.allAir.append(date)
#        self.allAir.append(fare)
        self.allAir = [self.code + ', ' + self.date + ', ' + self.fare]

    def __repr__(self):
        return str(self.allAir)

#a = Airlines("abc", '234', '300')
#b = Airlines("def", '122', '400')

abc = Airlines("abc", "22-33", "100")


print(abc.allAir)


#
#    def __repr__(self):
#        return str(self.allAir)
#
#def main():
#    airline1 = Airlines('AC111')
#    airline2 = Airlines('AC222')
#    airline1.setDate(250)
#    airline2.setDate(300)
#    airline1.setFare(1000)
#    airline2.setFare(3000)
#    print(airline1.code)
#
#if __name__ == "__main__":
#    main()
#
#print(Airlines.allAir)





