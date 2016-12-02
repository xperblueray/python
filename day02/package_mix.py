#!/usr/bin/pyhton3
# Filename: package_mix.py

def package_mix(*positions, **keywords):
    print(positions)
    print(keywords)


package_mix(1, 2, 3, a = 7, b = 8, c = 9)

