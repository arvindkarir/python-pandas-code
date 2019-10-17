# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:14:10 2017

@author: User
"""

#import os
import subprocess

def sevenzip(filename, zipname, password):
    print("Password is: {}".format(password))
    system = subprocess.Popen(["7z", "a", zipname, filename, "-p{}".format(password)])
    return(system.communicate())
    
sevenzip(r'C:\Users\User\Test\test', r'C:\Users\User\Test\backup.zip', 'secret')    