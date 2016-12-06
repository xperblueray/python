#!/usr/bin/python3
# Filename: out_params.py


def line_conf():
    b = 15
    def line(x):
        return 2*x + b
    b = 5
    return line


if __name__ == "__main__":
    my_line = line_conf()
    print(my_line(5))

