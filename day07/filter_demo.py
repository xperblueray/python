#!/usr/bin/python3
# Filename: filter_demo.py

def larger100(a):
    if a > 100:
        return True
    else:
        return False


for item in filter(larger100, [10, 56, 101, 500]):
    print(item)
