#!/usr/bin/python3
# Filename: vow.py

class Vow(object):
    def __init__(self, text):
        self.text = text
    def __enter__(self):
        self.txt = "I say: " + self.text
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.text = self.text + "!"


with Vow("I'm fine") as myVow:
    print(myVow.text)


print(myVow.text)

