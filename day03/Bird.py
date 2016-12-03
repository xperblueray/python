#!/usr/bin/python3
# Filename: Bird.py


class Bird(object):
    feather = True
    reproduction = "egg"
    def chirp(self, sound):
        print(sound)
    def set_color(self, color):
        self.color = color




summer = Bird()
print(summer.reproduction)
summer.chirp("jijiji")
summer.set_color("yellow")
print(summer.color)
