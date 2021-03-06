#!/usr/bin/python3
# Filename: decorate_class.py

def decorator_class(SomeClass):
    class NewClass(object):
        def __init__(self, age):
            self.total_display = 0
            self.wrapped        = SomeClass(age)

        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()

    return NewClass


@decorator_class
class Bird:
    def __init__(self, age):
        self.age = age

    def display(self):
        print("My age is", self.age)



if __name__ == "__main__":
    eagle_lord = Bird(5)
    for i in range(3):
        eagle_lord.display()


