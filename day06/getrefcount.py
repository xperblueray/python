#!/usr/bin/python3
# Filename: getrefcount.py

from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))

b = [a, a]
print(getrefcount(a))
