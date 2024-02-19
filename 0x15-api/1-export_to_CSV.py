#!/usr/bin/python3
""" script that use JSONPlaceholder API for getting informations about employee """
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    userr = f'{url}users/{userid}'
    ress = requests.get(userr)
    json_o = ress.json()
    namee = json_o.get('username')

    todos = f'{url}todos?userId={userid}'
    ress = requests.get(todos)
    tasks = ress.json()

    filename = f'{userid}.csv'
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in tasks:
            l_task = [userid, namee, task.get('completed'), task.get('title')]
            employee_writer.writerow(l_task)

