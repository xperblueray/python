#!/usr/bin/python3
# Filename: generator_demo.py


def gen():
    for i in range(4):
        yield i


# gen = (x for x in range(4))
