#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

# 1. The files and directions to be backed up are specified in a list
source = 'G:\\learnpython\\readme.md'

target_dir = 'G:'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'

rar_command = "WinRAR a %s %s -r" % (target, source)

if os.system(rar_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
