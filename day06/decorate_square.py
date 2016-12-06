#!/usr/bin/python3
# Filename: decorate_square.py


def square_sum(a, b):
    print("input:", a,b)
    return a**2 + b**2
def square_diff(a, b):
    print("Input: ", a, b)
    return a**2 - b**2

if __name__ == "__main__":
    print(square_sum(2, 5))
    print(square_diff(3, 5))
