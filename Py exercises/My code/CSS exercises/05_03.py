# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 21:00:44 2017

@author: User
"""
total, charges, fees, perMonth = 0, 0, 0, 0

def totalBill(plan, minute, new_user, student):
    if student == True:
        typeOf = True
    else:
        typeOf = False
    total = 1.13*(activation(new_user, student) + planType(plan, typeOf) + timeCost(plan, minute) )
    print(round(total,2))

def activation(new_user, student):
    if student == True or new_user == False:
        fees = 0.00
    else:
        fees = 20.0
    print('fees', fees)
    return float(fees)

def planType(plan, typeOf):
    if plan == 'A':
        perMonth = 40.00
        if typeOf == True:
            perMonth = 20.00
    elif plan == 'B':
        perMonth = 50.00
    else:
        perMonth = 100.00
    print('perMonth', perMonth)
    return float(perMonth)

def timeCost(plan, minute):
    charges = 0.0
    if plan == 'A':
        chargeTime = minute - 150
        if chargeTime <=0:
            charges == 0
        elif chargeTime >350:
            charges == 100
        else:
            charges = 0.50*chargeTime
    elif plan == 'B':
        chargeTime = minute - 250
        if chargeTime <=0:
            charges == 0
        elif chargeTime >570:
            charges == 80
        else:
            charges = 0.25*chargeTime
    else:
        charges = 0.0
    print('charges', charges)
    return float(charges)

totalBill('A', 80, True, True)
totalBill('B', 300, True, False)
totalBill('C', 300, False, False)