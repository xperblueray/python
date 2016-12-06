#!/usr/bin/python3
# Filename: env_demo.py

def line_conf():
    b = 15

    def line(x):
        return 2*x + b
    b = 5
    return line


if __name__ == "__main__":
    my_line = line_conf()
    print(my_line.__closure__)
    print(my_line.__closure__[0].cell_contents)

