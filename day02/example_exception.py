#!/usr/bin/python3
# Filename: example_exception.py

while True:
    inputStr = input("Please input a number:")

    try:
        num = float(inputStr)
        print("Input number:", num)
        print("result:", 10/num)
    except:
        print("Something Wrong.Try Again.")
