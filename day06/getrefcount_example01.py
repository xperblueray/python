from sys import getrefcount

a = [1, 3, 5]
b = a
print(getrefcount(b))

a = 1
print(getrefcount(b))
