# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:40:19 2018

@author: User
"""

class Airlines(object):
    ''' Fields: code(Str), dates(Int), price(Nat)'''

    allAirlines = []
    allCodes = []
    allDates = []
    allPrices = []
    registry = []

    def addAir(self, name, code, dates, price):
#        self.allAirlines.append(name)
#        self.allAirlines.append(code)
#        self.allAirlines.append(dates)
#        self.allAirlines.append(price)
        self.registry.append(self)

    def __init__(self, name, code, dates, price):
        self.name = name
        self.code = code
        self.dates = dates
        self.price = price

    def __str__(self):
        return "Code: {0.code}; Dates: {0.dates}; Price: {0.price}".format(self)

    def chooseAir(a1, a2):
        if a1.price > a2.price:
            print( True)
        else:
            print (False)

    def giveInfo(self):
        print(self.code, self.dates, self.price)

def main():
    airline1 = Airlines('airline1','AC027', 245, 600)
    airline2 = Airlines('airline2', 'AC027', 256, 800)
    airline3 = Airlines('airline3', 'AC115', 256, 700)
    airline4 = Airlines('airline4', 'AC028', 300, 400)
    airline1.addAir('airline1','AC027', 245, 600)
    airline2.addAir('airline2', 'AC027', 256, 800)
    airline3.addAir('airline3', 'AC115', 256, 700)
    airline4.addAir('airline4', 'AC028', 300, 400)
#    Airlines.chooseAir(airline4, airline1)
#    Airlines.giveInfo(airline1)
#    print(Airlines.allAirlines)

if __name__ == "__main__":
  main()

def theChooseFn(L, min, max):
    finalList = []
    for a in L:
        if a.dates > min and a.dates <= max:
            newL = [a.code, a.dates, a.price]
            finalList.append(newL)
    return finalList

print(theChooseFn(Airlines.registry, 250, 300))





#def binarySearch(L, d1, d2):
#    lower = 0
#    upper = len(L)
#    while lower < upper:
#        x = lower + (upper - lower) // 2
#        val = L.dates
#        if d1 == val:
#            return x
#        elif target > val:
#            if lower == x:   # this two are the actual lines
#                break        # you're looking for
#            lower = x
#        elif target < val:
#            upper = x



############################
# One way of doing it, possibly not acceptable within rubric
#def returnDates(L, d1, d2):
#    firstList = (list(filter(lambda x: (x[1] >=d1), L)))
#    secondList = (list(filter(lambda x: (x[1] <=d2), firstList)))
#    print(secondList)
#returnDates(allAirlines, 266,270)
#############################






#airline1 = Airlines('AC027',245,600)
#airline2 = Airlines('AC027', 256, 800)
#airline3 = Airlines('AC115', 256, 700)
#airline4 = Airlines('AC028', 300, 400)

#print(airline4.code)
#print(airline4)

#print(sorted(allAirlines, key = lambda x: (x[1] >266))) #this works
#print(list(filter(lambda x: (x[1] >266), allAirlines))) # this works as well