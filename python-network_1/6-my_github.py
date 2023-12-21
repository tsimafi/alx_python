import requests
import sys
import base64

def get_github_id(tsimafi,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):
    url = 'https://api.github.com/user'
    headers = {'Authorization': 'Basic ' + base64.b64encode((tsimafi + ':' + ).enc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ode()).decode('utf-8')}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()['id']
    else:
        return None

if name == 'main':
    if len(sys.argv) != 3:
        print("Usage: ./6-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    github_id = get_github_id(username, token)

    print(github_id)