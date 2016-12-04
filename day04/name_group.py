#!/usr/bin/python3
# Filename: name_group.py

import re

m = re.search("output_(?P<year>\d{4})", "output_1896.txt")
print(m.group("year"))
