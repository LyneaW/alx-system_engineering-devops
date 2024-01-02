#!/usr/bin/python3
"""Python script to export data in JSON format """


import json
import requests
import sys


if __name__ == "__main__":

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump({user.get('id'): [{
            "username": user.get('username'),
            "task": task.get('title'),
            "completed": task.get('completed')
        } for task in todo if user.get('id') == task.get('userId')]
            for user in users}, jsonfile)
