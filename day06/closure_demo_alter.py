#!/usr/bin/python3
# Filename: closure_demo_alter.py


def line_conf(a, b):
    def line(x):
        return a*x + b
    return line


line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
line3 = line_conf(5, 10)
line4 = line_conf(-2, -6)
