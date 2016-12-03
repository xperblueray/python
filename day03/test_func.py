#!/usr/bin/python3
# Filename: test_func.py

def test_func():
    try:
        m = 1/0
    except ValueError:
        print("Catch ValueError in the sub-function")
        try:
            test_func()
        except ZeroDivisionError:
            print("Catch error in the main program")
