#!/usr/bin/python3
# Filename: unpackage.py


def unpackage(a, b, c):
    print(a, b, c)


args = (1, 3, 4)
unpackage(*args)


args = {"a": 1, "b": 2, "c": 3}
unpackage(**args)
