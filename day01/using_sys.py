#!/usr/bin/python
# Filename: using_sys.py

import sys

print 'The command line arguments are:'
for i in sys.argv:
    print i
print '\n\nThe PTYHONPATH is ', sys.path, '\n'

