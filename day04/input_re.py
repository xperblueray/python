#!/usr/bin/python3
# Filename: input_re.py

import re


content = input("Please input your string: ")
m       = re.match("^ab.*c$", content)
print(m.group())


