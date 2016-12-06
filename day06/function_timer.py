#!/usr/bin/python3
# Filename: function_timer.py

import time

def function_timer(old_function):
    def new_function(*arg, **dict_arg):
        t1 = time.time()
        result = old_function(*arg, **dict_arg)
        t2 = time.time()
        print("The run time is:" + t + "s.")
        return result
    return new_function



