#!/usr/bin/python3
# Filename: prop_man.py

class Bird(object):
    feather = True


class Chicken(Bird):
    fly = False
    def __init__(self, age):
        self.age = age

    def get_adult(self):
        if self.age > 1.0:
            return True
        else:
            return False

    adult = property(get_adult)


summer = Chicken(2)
print(summer.adult)

summer.age = 0.4
print(summer.adult)


