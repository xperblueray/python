#!/usr/bin/python3
# Filename: reference_cycle.py

from sys import getrefcount



a = []
b = [a]
a.append(b)


print(getrefcount(a))
