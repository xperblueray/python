#!/usr/bin/python3
# Filename: example_for.py

interest_tuple = (0.01, 0.02, 0.03, 0.035, 0.05)

total = 500000

for interest in interest_tuple:
    repay = total * interest
    print("The interest of every year is : ", repay)
