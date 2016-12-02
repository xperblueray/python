#!/usr/bin/python3
# Filename: example_debug.py


while True:
    inputstr = input("Please input a number:")

    try:
        num = float(inputstr)
        print("Input number: ", num)
        print("Result:", 10/num)

    except ValueError:
        print("Illegal input. Try again.")
    except ZeroDivisionError:
        print("Illegal devision by zero. Try again.")
