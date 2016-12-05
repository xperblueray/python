#!/usr/bin/python3
# Filename: getattr_python.py

class Bird(object):
    feather = True


class Chicken(Bird):
    fly = False

    def __init__(self, age):
        self.age = age


    def __getattr__(self, name):
        if name == "adult":
            if self.age > 1.0:
                return True
            else:
                return False
        else:
            raise AttributeError(name)


summer = Chicken(2)
print(summer.adult)

summer.age = 0.5
print(summer.adult)

print(summer.male)



