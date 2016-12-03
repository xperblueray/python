#!/usr/bin/python3
# Filename: super.py

class Bird(object):
    def chirp(self):
        print("make sound")


class Chicken(Bird):
    def chirp(self):
        super().chirp()
        print("ji")


bird    = Bird()
bird.chirp()


summer  = Chicken()
summer.chirp()
