#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

# 1. The files and directions to be backed up are specified in a list
source = 'G:\\learnpython\\readme.md'
# 2. The backup must be stored in a main backup directory
target_dir = 'G:'
# 3. The files are backed up into a rar file.
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'

rar_command = "WinRAR a %s %s -r" % (target, source)
# Run the backup
if os.system(rar_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
