#!/usr/bin/python3
# Filename: package_position.py

def package_position(*all_arguments):
    print(type(all_arguments))
    print(all_arguments)


package_position(1, 4, 6)
package_position(5, 6, 7, 1, 2, 3)
