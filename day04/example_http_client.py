#!/usr/bin/python3
# Filename: example_http_client.py

import http.client
import pickle


conn       = http.client.HTTPConnection("www.baidu.com")
conn.request("GET", "/")
response   = conn.getresponse()



print(response.status, response.reason)
content    = response.read()
print(content)
