#!/usr/bin/python3
# Filename: attr_man.py

class Bird(object):
    feather = True

    def chirp(self):
        print("some sound")


class Chicken(Bird):
    fly = False

    def __init__(self, age):
        self.age = age


    def chirp(self):
        print("ji")



summer  = Chicken(2)
print("===> summer")
print(summer.__dict__)

print("===> Chicken")
print(Chicken.__dict__)


print("===> Bird")
print(Bird.__dict__)

print("===> object")
print(object.__dict__)

summer.chirp()
print("===> Show")
print(dir(summer))


autumn = Chicken(3)
autumn.feather = False
print(summer.feather)
print(autumn.feather)

print(autumn.__dict__)

