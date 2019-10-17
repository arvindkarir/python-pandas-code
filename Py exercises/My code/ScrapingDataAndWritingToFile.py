import csv
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup




URL = "http://www.bloomberg.com/quote/SPX:IND"
soup = BeautifulSoup(urlopen(URL), "lxml")


name_box = soup.find('h1', attrs={'class':'name'}) # Take out the <div> of name and get its value
name = name_box.text.strip() #take out <div> of name and get its value
price_box = soup.find('div', attrs={'class':'price'}) #the S&P index
price = price_box.text #the value
print(name, price) #screen

path = "C:\\Users\\User\\Desktop\\MIT EdX programming course\Py exercises\My code\SnP.csv" #define file name here
with open(path, 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])


















#find_string = str(soup.body.findAll(text = re.compile('Guaranteed high'))) #this finds the exact string
#find_string2 = soup.body.findAll(text = re.compile('Guaranteed high')) # not having str finds all strings with value
#find_string2 = soup.body.findAll(text = re.compile('the low'))
## Interestingly, a combination of find_string2 with two different values found the para with both values in it!!
#
#
#print(find_string) #the 'Guaranteed high'
#print(find_string2) #the forecast
