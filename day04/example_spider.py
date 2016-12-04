#!/usr/bin/python3
# Filename: example_spider.py

import http.client

conn      = http.client.HTTPConnection("www.xperblueray.com")
conn.request("GET", "/")
response  = conn.getresponse()


content = response.read()
content   = content.split(b"\r\n")

print(content)
