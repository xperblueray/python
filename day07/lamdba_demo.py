#!/usr/bin/python3
# Filename: lambda_demo.py

def square_sum(x, y):
    return x**2 + y**2


data_list1 = [1, 3, 5, 7]
data_list2 = [2, 4, 6, 8]

result     = map(square_sum, data_list1, data_list2)

for item in result:
    print(item)
