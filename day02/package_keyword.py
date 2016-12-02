#!/usr/bin/python3
# Filename: package_keyword.py

def package_keyword(**all_arguments):
    print(type(all_arguments))
    print(all_arguments)


package_keyword(a = 1, b = 9)
package_keyword(m = 2, n = 1, c = 11)
