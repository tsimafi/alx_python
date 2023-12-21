#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status using the requests package
"""

import requests

if name == "main":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))