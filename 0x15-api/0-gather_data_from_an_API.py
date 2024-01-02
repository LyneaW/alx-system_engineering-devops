#!/usr/bin/python3
""" returns information about employee's TODO list progress."""


import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()
    completed = []
    for task in todo:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task))
