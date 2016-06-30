#!/usr/bin/python
# filename: match.py

# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'hello')

result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo wj')
result3 = re.match(pattern,'helo wj')
result4 = re.match(pattern,'hello wj')

if result1:
    print result1.group()
else:
    print '1 match failure'

if result2:
    print result2.group()
else:
    print '2 match failure'

if result3:
    print result3.group()
else:
    print '3 match failure'

if result4:
    print result4.group()
else:
    print '4 match failure'
