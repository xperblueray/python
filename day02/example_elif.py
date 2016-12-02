#!/usr/bin/python3
# Filename: example_elif.py

i = 1

if i > 0:
    print("positive i")
    i = i + 1
elif i == 0:
    print("i is 0")
    i =  i * 10
else:
    print("negetive i")
    i = i - 1

