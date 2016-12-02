#!/usr/bin/python3
# Filename: devide_by_5_not_3.py

i    = 0
list = []
v    = True
while v:
    for j in range(1, 100):
        if((j%5 == 0) & (j%3 != 0)):
            list.append(j)
            i = i + 1
        else:
            continue
    v = False



print(list)


