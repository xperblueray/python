#!/usr/bin/python3
# Filename: params_transfer01.py

def f(x):
    x[0] = 100

    print(x)


a = [1, 2, 3]
f(a)
print(a)
