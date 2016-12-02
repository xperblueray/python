#!/usr/bin/python3
# Filename: residual.py


i = 0
residual = 500000.0
interest_tuple = (0.01, 0.02, 0.03, 0.035)
repay = 30000.0


while residual> 0:
    i = i + 1
    print("The ",i , "year need to pay debt")
    if i <= 4:
        interest = interest_tuple[i - 1]
    else:
        interest = 0.05
    residual = residual * (interest + 1) -repay

print("The residual is pay off at ",i ,"year.")
