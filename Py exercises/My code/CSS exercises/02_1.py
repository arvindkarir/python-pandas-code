# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:20:15 2017

@author: User
"""

def parking_costs(flag, timeIn, cost = 0):
    if flag == True:
        if timeIn >= 187:
            cost = 28.00
        else:
            timeIn = int(timeIn/20) + (timeIn%20 > 0)
            cost = timeIn*4
        print( "%.2f" % cost)
    else:
        if timeIn > 1.0 and timeIn <=4.285:
            cost = timeIn*28
        elif timeIn > 4.285 and timeIn < 7.0:
            cost = 120.00
        else:
            cost = (int(timeIn/7))*120 + (timeIn%7 > 0)*28
        print( "%.2f" % cost)

(parking_costs(False, 6))
(parking_costs(False, 29))
(parking_costs(True, 47))
(parking_costs(True, 500))