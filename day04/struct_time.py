#!/usr/bin/python3
# Filename: struct_time.py

import time

st = time.gmtime()
print(st)

st = time.localtime()
print(st)


st = time.mktime(st)
print(st)
