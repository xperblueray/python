#!/usr/bin/python3
# Filename: function_as_return.py


def line_conf():
    def line(x):
        return 2*x + 1
    return line

my_line = line_conf()

print(my_line(5))
