#!/usr/bin/python3
"""
Export all of the employee data in JSON format
"""
import json
import urllib.request as request

users_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'

if __name__ == '__main__':
    # users/employees
    with request.urlopen(users_url) as response:
        users = json.loads(response.read())

    # task todos
    with request.urlopen(todos_url) as response:
        todos = json.loads(response.read())

    # get employee usernames
    usernames = []
    for user in users:
        usernames.append([user.get('id'), user.get('username')])

    # get info about all employees in json format
    full_info = {}
    for username in usernames:
        employee_id = username[0]
        info = []
        for todo in todos:
            if todo.get('userId') == employee_id:
                info.append({
                    "username": username[1],
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                    })
        full_info[employee_id] = info

    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as json_file:
        json.dump(full_info, json_file)
