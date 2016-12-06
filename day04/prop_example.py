#!/usr/bin/python3
# Filename: prop_example.py

class num(object):
    def __init__(self, value):
        self.value = value

    def getneg(self):
        return -self.value

    def setneg(self, value):
        self.value = -value

    def delneg(self):
        print("value also deleted")
        del self.value


    neg = property(getneg, setneg, delneg, "I'm negative")


x = num(1.1)
print(x.neg)
x.neg = -11
print(x.value)
print(num.neg.__doc__)
del x.neg
