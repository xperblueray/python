#!/usr/bin/python3
# Filename: params_transfer.py

def f(x):
    print(id(x))
    x = 100
    print(id(x))
    


a = 1
print(id(a))

f(a)
print(a)


