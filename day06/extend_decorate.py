#!/usr/bin/python3
# Filename: extend_decorate.py

def decorate_demo(old_function):
    def new_function(a, b):
        print("Input: ", a, b)
        return old_function(a, b)
    return new_function

@decorate_demo
def square_sum(a, b):
    return a**2 + b**2

@decorate_demo
def square_diff(a, b):
    return a**2 - b**2

if __name__ == "__main__":
    print(square_sum(3, 4))
    print(square_diff(3, 4))

