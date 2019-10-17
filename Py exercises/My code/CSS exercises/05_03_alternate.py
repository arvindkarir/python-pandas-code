# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:44:43 2018

@author: User
"""

def phone_bill(plan, minute, new_user, student):
    monthly_fees = {'A':40.00, 'B':50.00, 'C':100.00}
    free_minutes = {'A':150, 'B':250, 'C':10000}
    per_minute = {'A':0.50, 'B':0.25, 'C':0}
#    cap_of_minute_charges = {'A':100, 'B':80, 'C':0}
    activation_fee_rate = {'A':20, 'B':20, 'C':20}
    charge_minutes = activation_fee = 0
    find_minutes = minute - free_minutes[plan]
    if find_minutes >0:
        bill_minutes = find_minutes
    else:
        bill_minutes = 0
    billable_minutes = (bill_minutes)*per_minute[plan]
#    print(billable_minutes,'billed minutes')
    if plan == 'A' and billable_minutes >= 100:
        charge_minutes = billable_minutes
    if plan == 'B' and billable_minutes <= 80:
        charge_minutes = billable_minutes
    if student == True and plan == 'A':
        monthly_fees[plan] *= 0.50
    if new_user == True and student == False:
        activation_fee = activation_fee_rate[plan]

    bill_total = 1.13*(monthly_fees[plan]+ charge_minutes + activation_fee)
    print("%.2f" % round(bill_total,2))


phone_bill('A', 80, True, True)
phone_bill('B', 300, True, False)
phone_bill('C', 300, False, False)