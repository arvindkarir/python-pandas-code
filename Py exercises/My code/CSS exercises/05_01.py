# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 13:41:53 2017

@author: User
"""
import math

def compareArea(circum, width):
    circleA = (circum*circum)/(4*math.pi)
    squareA = width*width
    if circleA == squareA:
        print("tie")
    elif circleA >= squareA:
        print("circle")
    else:
        print("square")

compareArea(0.0, 0.0)
compareArea(10.4, 4.0)
