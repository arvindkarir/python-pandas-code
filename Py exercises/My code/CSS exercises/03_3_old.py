# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:30:46 2017

@author: User
"""

def scorePwd():
    score = 0
    s1 = str(input('Enter your pwd\n'))
    if checkVals(s1) == True:
        print('Your password meets valid character set, and this is what you entered\n', s1)
    else:
        return ('Invalid password')
    lenOf = len(s1)
    if lenOf < 5:
        score -= 10
    elif lenOf > 8:
        score += 15
    print( score)


def checkVals(s1):
    flagChk = False
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvwxyz'
    andDigits = '0123456789'
    splChrs = '~!@#$%^&*()_+=` ?><'
    for c in s1: #for each and every letter
        if c in UCLetters or c in LCLetters or c in andDigits or c in splChrs:
            flagChk = True
        else:
            flagChk = False
    return flagChk

scorePwd()

#    onebit = s1[0].lower()
#    twobit = s2[-4:].lower()
#    lastbit = s3[::-1]
#    lastbitRev = lastbit[1:4]
#    print(onebit + twobit + lastbitRev)


# Dictionary type implementation
#    if pwd.islower() and pwd.isupper() and pwd.isdigit():
#        print ('score is weak')
#
#    scores = {0:'Weak', 1:'Medium', 2:'Strong', 3:'Super'}
#    strength = dict.fromkeys(['has_upper', 'has_lower', 'has_num', 'has_spl'], False)
#    if re.search(r'[A-Z]', pwd):
#        strength['has_upper'] = True
#    if re.search(r'[a-z]', pwd):
#        strength['has_lower'] = True
#    if re.search(r'[0-9]', pwd):
#        strength['has_num'] = True
#    if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', pwd):
#        strength['has_spl'] = True
#
#    score = len([b for b in strength.values() if b])
#
#    print ('Password is %s' % scores[score])