#!/usr/bin/python3
"""
Export employee data in CSV fromat
"""
import csv
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

    # get the employee name
    for user in users:
        if user.get('id') == employee_id:
            employee_name = user.get('name')
            break

    # get all the tasks with their status
    # for a certain employee
    tasks = []
    for todo in todos:
        if todo.get('userId') == employee_id:
            tasks.append([todo.get('completed'), todo.get('title')])

    file_name = f'{employee_id}.csv'

    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id] + [employee_name] + task)
