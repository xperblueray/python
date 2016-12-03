#!/usr/bin/python3
# Filename: context_manager.py

# Use the context manager

with open("new.txt", "w") as f:
    f.write("Hello World!")

print(f.closed)
