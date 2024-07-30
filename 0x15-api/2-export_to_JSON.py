#!/usr/bin/python3
"""
Export employee data in JSON format
"""
import json
import sys
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

    # the id of the employee we want info for
    employee_id = int(sys.argv[1])

    # get the employee username
    for user in users:
        if user.get('id') == employee_id:
            employee_username = user.get('username')
            break

    # get info about a particular employee
    info = []
    for todo in todos:
        if todo.get('userId') == employee_id:
            info.append({
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": employee_username
                })
    full_info = {employee_id: info}
    file_name = f'{employee_id}.json'

    with open(file_name, 'w') as json_file:
        json.dump(full_info, json_file)
