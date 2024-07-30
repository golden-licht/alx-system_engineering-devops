#!/usr/bin/python3
"""
For a given employee ID, passed as arguement, prints information
about his/her TODO list progress, fetching from an API
"""

import json
import sys
import urllib.request as request

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

if __name__ == '__main__':
    # users/employees
    with request.urlopen(users_url) as response:
        users = json.loads(response.read())

    # task todos
    with request.urlopen(todos_url) as response:
        todos = json.loads(response.read())

    # the id of the employee we eant info for
    employee_id = int(sys.argv[1])

    # get the employee name
    for user in users:
        if user.get('id') == employee_id:
            employee_name = user.get('name')
            break

    # get the tasks done by certain employee
    total_taks = 0
    tasks_done = []
    for todo in todos:
        if todo.get('userId') == employee_id:
            total_taks += 1
            if todo.get('completed'):
                tasks_done.append(todo.get('title'))

    # print the info
    print(
        f'Employee {employee_name} is done with tasks'
        f'({len(tasks_done)}/{total_taks}):'
    )
    for task in tasks_done:
        print(f'\t {task}')
