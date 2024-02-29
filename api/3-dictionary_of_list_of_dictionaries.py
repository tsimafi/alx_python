#!/usr/bin/python3
import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit()

    employee_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200:
        print('User not found')
        exit()
    if todo_response.status_code != 200:
        print('Todos not found')
        exit()

    user_data = user_response.json()
    todo_data = todo_response.json()

    username = user_data.get('username')

    tasks = []
    for todo in todo_data:
        task_info = {
            "username": username,
            "task": todo.get('title'),
            "completed": todo.get('completed'),
        }
        tasks.append(task_info)

    filename = "{}.json".format(employee_id)
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=4)

    print("Data exported to", filename)
