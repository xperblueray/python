from sys import getrefcount
a = []

a.append(a)
print(getrefcount(a))
