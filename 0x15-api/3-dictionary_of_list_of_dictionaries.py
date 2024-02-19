#!/usr/bin/python3
"""
Exportss data in JSON format
"""

import json
import requests


def main():
    """
    main functionn to run the scriptt
    """
    with requests.Session() as session:
        users = session.get(
            "https://jsonplaceholder.typicode.com/users").json()
        todos = session.get(
            'https://jsonplaceholder.typicode.com/todos').json()

    todo_alll = {}
    for u in users:
        task_list = [
            {
                "username": u.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todos if task.get('userId') == u.get('id')
        ]
        todo_alll[u.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(todo_alll, file)


if __name__ == "__main__":
    main()
