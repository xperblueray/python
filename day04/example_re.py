#!/usr/bin/python3
# Filename: example_re.py

import re

m      = re.search("[0-9]", "0ab2cd4ef9")
print(m.group(0))
