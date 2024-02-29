import sys
import requests

# Function to fetch employee data from the API
def fetch_employee_data(employee_id):
    try:
        # Fetch employee details
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        response.raise_for_status()
        employee_data = response.json()
        
        # Fetch employee's TODO list
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
        response.raise_for_status()
        todos_data = response.json()
        
        return employee_data, todos_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

# Function to calculate and display TODO list progress
def display_todo_progress(employee_id):
    employee_data, todos_data = fetch_employee_data(employee_id)
    
    # Extract relevant information
    employee_name = employee_data['name']
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])
    completed_task_titles = [todo['title'] for todo in todos_data if todo['completed']]
    
    # Display progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task_title in completed_task_titles:
        print(f"\t{task_title}")

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
    
    display_todo_progress(int(employee_id))
