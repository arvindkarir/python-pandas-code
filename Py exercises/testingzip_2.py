# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import time
import subprocess


#Create target directory if it is not present
#if not os.path.exists(target_dir):
#    os.mkdir(target_dir) # make directory

def sevenzip(password):
    source = r'C:\Users\User\Test\test'
    target_dir = r'C:\Users\User\Test\backup'
    target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
    print("Password is: {}".format(password))
    system = subprocess.Popen(["7z", "a", 'target', 'source', "-p{}".format(password)])
    return(system.communicate())

    
  
    
    
#    
##zip_command = '7z a -i[r[-|0]]{@listfile|!wildcard}:' target
### Run the backup
##print('Zip command is:')
##print(zip_command)
##print('Running:')
#if os.system(zip_command) == 0:
#    print('Successful backup to', target)
#else:
#    print('Backup FAILED')
    
    
sevenzip( 'secret')