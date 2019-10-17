# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:20:15 2017

@author: User
"""

def interestRate(balanceOf, typeOf, levelOf):
    levelAC = ('Platinum', 'Gold', 'Standard')
    typeAC = ('Personal', 'Business')
    if levelOf in levelAC and typeOf in typeAC and balanceOf >=0:
        if 'Personal' in typeOf:
            personalInterest(balanceOf, levelOf)
        else:
            businessInterest(balanceOf, levelOf)
    else:
        print('Please see customer service')
    return

def personalInterest(balanceOf, levelOf):
    if levelOf == 'Standard':
       if balanceOf >= 0:
           print('ROI is 1.2%')
       else:
           print('Minimum balance is negative')
    elif levelOf == 'Gold':
        if balanceOf >= 2000 and balanceOf < 5000:
            print('ROI is 1.9%')
        elif balanceOf >= 5000:
            print('ROI is 2.3%')
        else:
            print('ROI is zero% for this personal account')
    else:
        print('Unknown account level')
    return

def businessInterest(balanceOf, levelOf):
    if levelOf == 'Standard':
       if balanceOf < 2500:
           print("ROI is zero% for this business account")
       else:
           print('ROI is 1.75%')
    elif levelOf == 'Platinum':
        if balanceOf < 2500:
            print("ROI is zero% for this business account")
        elif balanceOf >= 2500 and balanceOf < 10000:
                print('ROI is 1.75%')
        else:
            balanceOf >= 10000
            print('ROI is 2.6%')
    else:
        print("Unknown Business account")
    return
interestRate(10500, 'Business', 'Gold')
interestRate(2200, 'Business', 'Standard')
interestRate(500.56, 'Personal', 'Gold')
interestRate(10500, 'Personal', 'Gold')
interestRate(4500, 'Personal', 'Gold')
interestRate(-4500, 'Personal', 'Standard')
interestRate(-4500, 'Personal', 'Platinum')
interestRate(4000, 'Personal', 'Platinum')