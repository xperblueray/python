#!/usr/bin/python3
# Filename: change_list.py


b = [1, 2, 3]

def change_list(b):
    b[0] = b[0] + 1
    return b

print(change_list(b))
print(b)

