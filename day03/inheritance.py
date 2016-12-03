#!/usr/bin/python3
# Filename: inheritance.py

class Bird(object):
    feather      = True
    reproduction = "egg"
    def chirp(self, sound):
        print(sound)


class Chicken(Bird):
    how_to_move = "walk"
    edible      = True


class Swan(Bird):
    how_to_move = "swim"
    edible      = False


summer = Chicken()
print(summer.feather)
summer.chirp("ji")
