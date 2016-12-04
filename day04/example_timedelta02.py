#!/usr/bin/python3
# Filename: example_timedelta02.py


from datetime import datetime


format     = "%Y-%m-%d %H:%M"
t          = datetime(2012, 9, 5, 23, 30)


print(t.strftime(format))

