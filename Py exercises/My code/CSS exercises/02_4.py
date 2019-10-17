# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:53:47 2017

@author: User
"""

def redMod(top, bot):
    if top == bot or top < bot:
        print('check values')
    elif top < 0 or bot < 0:
        raise ValueError
    else:
        bal = top - bot
        if bal > bot:
            redMod(top - bot, bot)
        else:
            print( bal)

redMod(1400, 500)