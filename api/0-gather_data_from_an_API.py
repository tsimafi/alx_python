import sys
import requests

def fetch_employee_data(employee_id):
    # Fetching employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    if response.status_code != 200:
        print(f"Failed to fetch employee data for ID {employee_id}.")
        return None
    employee_data = response.json()
    
    # Fetching employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    if response.status_code != 200:
        print(f"Failed to fetch TODO list for employee {employee_data['name']}.")
        return None
    todo_list = response.json()
    
    return employee_data, todo_list

def display_todo_progress(employee_data, todo_list):
    completed_tasks = [task for task in todo_list if task['completed']]
    total_tasks = len(todo_list)
    completed_count = len(completed_tasks)
    
    # Displaying progress
    print(f"Employee {employee_data['name']} is done with tasks ({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
