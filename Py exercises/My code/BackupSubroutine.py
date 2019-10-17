import os
import time

source = [' "C:\\Users\\User\\Dropbox\\Poetry posts" ']
target_dir = "C:\\Users\\User\\Desktop\\MIT EdX programming course"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')
# Take a comment from the user to
# create the name of the zip file
comment = input('Enter a comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))
# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
