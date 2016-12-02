#!/usr/bin/python3
# Filename: print_arguments.py

def print_arguments(a, b, c):
    """print arguments according to their sequence"""
    print(a, b, c)


print_arguments(1, 3, 5)
print_arguments(5, 3, 1)
print_arguments(3, 5, 1)


print_arguments(c=5, b=3, a=1)

print_arguments(1, c=5, b=3)


# default arguments

def f(a, b, c = 10):
    return a + b + c



print(f(3, 2, 1))
print(f(3, 2))


