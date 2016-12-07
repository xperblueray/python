#!/usr/bin/python3
# Filename: reduce_demo.py


from functools import reduce

data_list = [1, 2, 5, 7, 9]
result = reduce(lambda x, y: x + y, data_list)
print(result)
