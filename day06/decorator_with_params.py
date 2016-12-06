#!/usr/bin/python3
# Filename: decorator_with_params.py

def pre_str(pre=""):
    def decorator(old_function):
        def new_function(a, b):
            print(pre + "input", a, b)
            return old_function(a, b)
        return new_function
    return decorator


@pre_str("^_^")
def square_sum(a,b):
    return a**2 + b**2

@pre_str("T_T")
def square_diff(a, b):
    return a**2 - b**2

if __name__ == "__main__":
    print(square_sum(2, 5))
    print(square_diff(2, 5))



