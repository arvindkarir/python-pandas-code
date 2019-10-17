# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:21:47 2018

@author: User
"""
'''
# using class - not sure how to sort tho

class Airlines:
    def __init__(self, air_code, flight_dates, prices):
        self.air_code = air_code
        self.flight_dates = flight_dates
        self.prices = prices
        print('Flight record for %s created' % self.air_code)

    def description(self):
        desc_str = "%s, %s, %s" %(self.air_code, self.flight_dates, self.prices)
        return desc_str

    def choose_flight( date1, date2):
        match_flights = []
        for each in all_airlines:
            if each.flight_dates >= date1 and each.flight_dates <= date2:
                match_flights.append(each.description())
        print(match_flights) # this is not sorted by price

all_airlines = [Airlines('AC027', 245, 600), Airlines('AC027', 256, 800),
Airlines('AC115', 256, 700), Airlines('AC028', 300, 400)]

Airlines.choose_flight( 250,350) '''

def choose_flight(all_airlines, date1, date2):
    match_flights = []
    for each in all_airlines:
        if each[1]>= date1 and each[1] <= date2:
            print(each[1])
            match_flights.append(each)
    print(match_flights)
    # Now for linear sort by price
    for i in range(len(match_flights)):
        key = match_flights[i][2]
        position = i
        while position > 0 and match_flights[position-1][2]:
            match_flights[position][2] = match_flights[position-1][2]
            position = position - 1
    match_flights[position][2] = key
    print(match_flights)


#    print(match_flights.sort(key = lambda x: x[0], reverse = True))

all_airlines = [['AC027', 245, 600], ['AC027', 256, 800],
['AC115', 256, 700], ['AC028', 300, 400]]

choose_flight(all_airlines,250,350)
