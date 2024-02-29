import sys
import json
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

# Function to export data to JSON file
def export_to_json(employee_id, employee_data, todos_data):
    try:
        filename = f"{employee_id}.json"
        with open(filename, mode='w') as file:
            json.dump({str(employee_id): [{"task": todo['title'], "completed": todo['completed'], "username": employee_data['username']} for todo in todos_data]}, file)
        print(f"Data exported to {filename}")
    except Exception as e:
        print(f"Error exporting to JSON: {e}")

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
    
    employee_id = int(employee_id)
    employee_data, todos_data = fetch_employee_data(employee_id)
    export_to_json(employee_id, employee_data, todos_data)
