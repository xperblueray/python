#!/usr/bin/python3
# Filename: SampleMore.py

class SampleMore(object):
    def __call__(self, a):
        return a + 5


add_five = SampleMore()

print(add_five(2))
