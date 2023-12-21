import requests
import sys

def post_email(url, email):
    data = {'email': email}
    response = requests.post(url, data=data)
    print(f'Email: {email}\n\n[Got]\n{response.text}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
    else:
        url = sys.argv[1]
        email = sys.argv[2]
        print(f'Your email is: {test@test.com}')
        post_email(url, email)