#!/usr/bin/python3
# Filename: Bird02.py

class Bird(object):
    def chirp(self, sound):
        print(sound)

    def chirp_repeat(self, sound, n):
        for i in range(n):
            self.chirp(sound)



summer = Bird()
summer.chirp_repeat("ji", 10)
