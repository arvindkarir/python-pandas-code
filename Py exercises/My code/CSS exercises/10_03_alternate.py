# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:55:54 2018

@author: User
"""

class loans():
    ''' str(ID), str(project), str(country), str(code), orig_amount, cancel_amount'''
    def __init__(self, ID, project, country, code, orig_amount, cancel_amount):
        self.ID = ID
        self.project = project
        self.country = country
        self.code = code
        self.orig_amount = orig_amount
        self.cancel_amount = cancel_amount

    def balance(self):
        self.balance = float(self.orig_amount) - float(self.cancel_amount)
        return ( format(self.balance, '.2f') )

    def description(self):
        desc_str = "%s  %s" %(self.ID, self.project)
        return desc_str

def make_instances(data):
    fields = (data.split('\t'))
    loan_data = loans( fields[0], fields[1], fields[2].split( '(' )[0], fields[2].split( '(' )[1].strip(  ' )' ), ((fields[3]).split(' / ')[0].strip('$')), (fields[3]).split(' / ')[1].strip('$') )
    return loan_data


def make_data(infile):
    f = open(infile, 'r')
    loan_data = map(make_instances, f.readlines() )
    f.close()
# just to get print out of various values
#    for each in loan_data:
#        print( each.country,'\t', each.ID, '\t', each.balance() )
#        print (each.description())
#
#    the code below is working...
#    loan_dict = {}
#    for each in loan_data:
#        balance = format(float(each.orig_amount) - float(each.cancel_amount), '.2f')
#        if each.country in loan_dict:
#            loan_dict[each.country] = [loan_dict[each.country]] + [each.ID +', ' + (str(balance))]
#        else:
#            loan_dict[each.country] = [each.ID + ', ' + str(balance)]
#    print(loan_dict)

    another_dict = {}
    for each in loan_data:
        balance = format(float(each.orig_amount) - float(each.cancel_amount), '.2f')
#        print(balance)
#        print(each.description().split(' ')[:-1])
        if each.country in another_dict:
            another_dict[each.country] = another_dict[each.country] + [each.description() + '\t'+ balance]
        else:
            another_dict[each.country] = [each.description()+ '\t'+ balance]

    first_line = out_list = []
    for k, v in another_dict.items():
        running_balance = 0
#        print(k,v)
        count = len(v)
        out_list = []
        for each in v:
            out_list += [each.split('\t')]
            running_balance += float(each.split('\t')[-1])
        first_line += [k + 'has '+ str(count) + ' loan/s, total of ' + str(running_balance)]
        first_line.append(out_list)

    final_list = []
    for i,j in enumerate(first_line):
        if i%2 == 0:
            print(j)
            final_list.append(j)
        else:
            for k in range(len(j)):
                print(j[k])
                final_list.append(j[k] )

    summary_file(final_list)

def summary_file(thelist):
    loanfile = open("summary_alternate.txt","w")
    for each in thelist:
        s = '{0}\n'
        loanfile.write( s.format(each))
    loanfile.close()



make_data('worldbank_small.txt')

# just for kicks - experiment
#    loan_list = []
#    for country in loan_data:
#        print(country.description(country), loans.balance(country),'\n')
#        loan_list.append(str(country.description(country))+ '  ' + str(loans.balance(country) ))
#    print(loan_list)