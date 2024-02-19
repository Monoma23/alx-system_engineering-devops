#!/usr/bin/python3
""" script converting data to json """


import json
import requests
import sys


if __name__ == "__main__":
    userrId = sys.argv[1]
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(userrId)
            )

    name = user.json().get('username')
    todoss = requests.get('https://jsonplaceholder.typicode.com/todoss')

    todooUser = {}
    taskList = []

    for taskk in todoss.json():
        if taskk.get('userrId') == int(userrId):
            taskDict = {
                    "taskk": taskk.get('title'),
                    "completed": taskk.get('completed'),
                    "username": user.json().get('username')
                    }
            taskList.append(taskDict)
        todooUser[userrId] = taskList

    filename = userrId + '.json'

    with open(filename, mode="w") as f:
        json.dump(todooUser, f)

