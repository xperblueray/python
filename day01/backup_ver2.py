#!/usr/bin/bash
# Filename: backup_ver2.py

import os
import time

# 1. The files and directories to be backed up are specified in a list
source = ['/home/blueray/Project/python']
# If you are using Windows, use source = [r'C:\Documents', r'C:\work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = '/mnt/h/File/backup/'
# Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directorhy
today = target_dir +time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

#Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make a directory
    print 'Successfully created directory', today

# The name of the zip file
target = today + os.sep + now +'.zip'

# 5. We use the ziip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup Failed'
