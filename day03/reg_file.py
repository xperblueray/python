#!/usr/bin/python3
# Filename: reg_file.py

# regular file behavior

f = open("new.txt", "w")
print(f.closed)
f.write("Hello World!")
f.close()


print(f.closed)
