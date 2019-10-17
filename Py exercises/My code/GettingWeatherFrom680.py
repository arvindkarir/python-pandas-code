# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:58:02 2017
First attempt at scraping some data from a website
@author: User
"""
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = "http://www.680news.com/weather/"
soup = BeautifulSoup(urlopen(URL), "lxml")
find_string = soup.body.findAll(text = re.compile('Guaranteed high')) #this finds the exact string
#find_string2 = soup.body.findAll(text = re.compile('Guaranteed high')) # not having str finds all strings with value
find_string2 = soup.body.findAll(text = re.compile('weather forecast'))
# Interestingly, a combination of find_string2 with two different values found the para with both values in it!!


#print(find_string) #the 'Guaranteed high'
#print(find_string2) #the forecast






find_string3 = soup.body.findAll(id="wg-guarantee")

print(find_string, find_string2, find_string3)