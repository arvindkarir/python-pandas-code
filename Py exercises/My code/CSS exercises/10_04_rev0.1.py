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

    def getinfo(self, country):
        print( self.ID, self.project)

    def __repr__(self):
        s = "Loan ID {0.ID} for project {0.project}, of country {0.country}, code {0.code}, for amount {0.amount}, repaid {0.canceled}"
        return s.format(self)

def strtoloan(s):
    fields = s.split("\t")
    data = Loan(fields[0], fields[1], fields[2].split( '(' )[0], fields[2].split( '(' )[1].strip(  ' )' ), ((fields[3]).split(' / ')[0].strip('$')), (fields[3]).split(' / ')[1].strip('$') ) # scrubbing off the data in each instance
    return data

def getdata(inputfilename):
    loanfile = open(inputfilename, 'r')
    loans = map(strtoloan, loanfile.readlines()) # map the function to iter
    loanfile.close()
    loaninfo = []
    loandict = {}
    for l in loans:
        balance = round((float(l.amount) - float(l.canceled)), 2) # calculating the remainder of loan
        loaninfo.append( [l.country, l.ID, l.project, balance] ) # capturing info in one file
        if l.country in loandict: # add balance for multiple loans for summary
            loandict[l.country] = loandict[l.country] + ', ' + (str(balance))
        else:
            loandict[l.country] = str(balance)
    loandictsorted = (sorted(loandict.items()) )
    summaryfile(loandictsorted)
    countries = [item for item in loandict]
    loansforeach = [ loandict[item] for item in loandict]
    totaleach = []
# this below is a mind bending exercise and the loan/s count is not even done yet!!
    for each in loansforeach:
        andtotal = 0.00
        for i in (each.split(',')):
            andtotal += float(i.strip(' '))
        totaleach.append(andtotal)
    print(list(zip(countries, (totaleach) ) ) )

def summaryfile(thelist):
    loanfile = open("summary.txt","w")
    for each in thelist:
        s = '{0}\n'
        loanfile.write( s.format(each))
    loanfile.close()




getdata("worldbank.txt")

#def dosome(l):
#    countryloan = {}
#    for each in l:
#        countryloan[each[0]] = (each[3])
#    print(countryloan)
#    for key, value in countryloan.items():
#        if key in countryloan:
#            print( key, countryloan[key])
#            key = key + str(countryloan[key])
#        else:
#            key =  str(countryloan[key])
#    print(countryloan)
