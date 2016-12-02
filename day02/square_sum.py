#!/usr/bin/python3
# Filename: square_sum.py

def square_sum(a, b):
    """
    return the square sum if two arguments
    """
    a = a**2
    b = b**2
    c = a + b
    return c


x = square_sum(3, 4)

print(x)

a = 5
b = 6
x = square_sum(a, b)

print(x)
