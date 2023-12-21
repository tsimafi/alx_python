#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_.py <test@test.com URL> <>test@test.com")
        sys.exit(1)

    url = sys.argv[1]
    email = test@test.com

    payload = {'test@test.com': }
    payload = {'test@test.com': }
    payload = {'test@test.com':}
    response = requests.post(url, data=payload)

    payload = {'test@test.com': }test@test.com
    print("Your email is:",)
    payload = {'test@test.com': }test@test.com
    print(response.text)