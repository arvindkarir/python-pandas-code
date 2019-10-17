# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:29:22 2018

@author: User
"""

class Loan:
    'Fields: ID-->str, project-->str, country-->str, principal-->float, cancelled-->float. A loan is an object loan(ID, project, country, principal, cancelled)'
    def __init__(self, ID, project, country, code, amount, canceled):
        self.ID = ID
        self.project = project
        self.country = country
        self.code = code
        self.amount = amount
        self.canceled = canceled

    def __repr__(self):
        s = "Loan ID {0.ID} for project {0.project}, of country {0.country}, code {0.code}, for amount {0.amount}, repaid {0.canceled}"
        return s.format(self)

def strtoloan(s):
    fields = s.split("\t")
    data = Loan(fields[0], fields[1], fields[2].split( '(' )[0], fields[2].split( '(' )[1].strip(  ' )' ), ((fields[3]).split(' / ')[0].strip('$')), (fields[3]).split(' / ')[1].strip('$') )
    return data

def getdata(inputfilename):
    loanfile = open(inputfilename, 'r')
    loans = map(strtoloan, loanfile.readlines())
    loanfile.close()
#    print(list(loans) )
    loandict = {}
    for l in loans:
        balance = round((float(l.amount) - float(l.canceled)), 2)
        if l.country in loandict:
            loandict[l.country] = loandict[l.country] + ', ' + (str(balance))
        else:
            loandict[l.country] = str(balance)
    print(loandict)
#    longdict={}
#    for l in loans:
#        longdict[l.country] = [str(l.ID)]
#    print(list(longdict.items()) )
#        writedata(key, value)

#def writedata(country, balance):
#    otherfile = open("summary.txt", "w")
#    otherfile.writelines(country)
#    otherfile.close()



getdata("worldbank.txt")
