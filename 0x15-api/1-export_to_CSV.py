#!/usr/bin/python3

""" Python script to export data in the CSV format """


import csv
import requests
import sys


if __name__ == "__main__":

    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([user_id, user.get('username'),
                             task.get('completed'), task.get('title')])
