# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 13:52:01 2017

@author: User
"""
import re

aPara = "this is a list of words. and here is another"


def splitLine(aPara):
    sList = [item.strip() for item in re.split('[!?.]', aPara) if item]
    print(sList)

splitLine(aPara)
#
#print(aPara.split())
#print(len(aPara.split()))
