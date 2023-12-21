#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response.
"""

import requests
import sys

if name == "main":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print("Your email is:", email)
    print(response.text)