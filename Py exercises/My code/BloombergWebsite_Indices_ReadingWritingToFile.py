# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:14:40 2017
https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
@author: User
"""
# List of couple of indices from Bloomberg

import csv
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

urls = ('http://www.bloomberg.com/quote/SPX:IND','http://www.bloomberg.com/quote/CCMP:IND') #note use of brackets, square brackets yield a tuple which does not have attribute timeout, hence AttributeError

# for loop
data = []
for pg in urls:
    soup = BeautifulSoup(urlopen(pg), 'html.parser')

# Take out the <div> of name, get value
    name_box = soup.find('h1', attrs={'class':'name'})

# take out <div> of name, get its text
    name = name_box.text.strip()

# the value of index
    price_box = soup.find('div', attrs={'class':'price'})
# and its text
    price = price_box.text

# make dataset
    data.append((name, price))

path = "C:\\Users\\User\\Desktop\\MIT EdX programming course\Py exercises\My code\Indices.csv" #define file name here
with open(path, 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name, price in data:
        writer.writerow([name, price, datetime.now()])