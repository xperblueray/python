#!/usr/bin/python3
# Filename: function_as_return01.py

def line_conf():
    def line(x):
        return 2*x + 1
    print(line(5))


if __name__ == "__main__":
    line_conf()
    print(line(5))

