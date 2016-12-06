#!/usr/bin/python3
# Filename: curve_closure_demo.py

def curve_closure(a, b, c):
    def curve(x):
        return a*x**2 + b*x + c
    return curve


curve1 = curve_closure(1, 2, 1)
