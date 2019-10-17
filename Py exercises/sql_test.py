# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 10:59:40 2018

@author: User
"""

import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)
cursor.execute("SELECT * FROM employee")
print("\nfetch one:")
res = cursor.fetchone()
print(res)










#
#
#connection.commit()
#
#connection.close()