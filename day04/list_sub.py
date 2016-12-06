#!/usr/bin/python3
# Filename: list_sub.py

class SuperList(list):
    def __sub__(self, b):
        a = self[:]
        b = b[:]

        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a



print(SuperList([1, 2, 3]) - SuperList([3, 4]))

