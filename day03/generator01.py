#!/usr/bin/python3
# Filename: generator01.py


def gen():
    i = 0
    while i < 10000000:
        i = i + 1
        yield i


for i in gen():
    print(i)
