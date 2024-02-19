#!/usr/bin/python3
""" Script uses JSONPlaceholder API for getting information about employee """
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get(f'{url}users/{sys.argv[1]}').json()
    print(f"Employee {user.get('name')} is done with taskss", end="")

    taskss = requests.get(f'{url}todos?userId={sys.argv[1]}').json()
    completedTasks = [taskk for taskk in taskss if taskk.get('completed')]

    print(f"({len(completedTasks)}/{len(taskss)}):")
    for taskk in completedTasks:
        print(f"\t {taskk.get('title')}")
