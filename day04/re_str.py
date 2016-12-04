#!/usr/bin/python3
# Filename: re_str.py

import re


content = "abcd_output_1994_abcd_1912_abcd"

m       = re.search("output_(\d{4})", content)
print(m.group(1))
