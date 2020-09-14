#!/usr/bin/python3
""" Is a script that make a request to JSON """


import json
import requests
import sys


if __name__ == "__main__":
    user_id = None
    url = 'https://jsonplaceholder.typicode.com/'

    # check if the argument is a number
    if len(sys.argv) > 0:
        user_id = int(sys.argv[1]) if sys.argv[1].isdigit() else None

    if user_id and user_id < 11:
        # to get the user name
        infor_user = requests.get('{}users/{}'.format(url, user_id))

        # to print the task
        tasks_complete = requests.get(
            '{}todos?userId={}&completed=true'.format(url, user_id)
        )

        # the whole tasks
        tasks = requests.get(
            '{}todos?userId={}'.format(url, user_id)
        )

        user_name = json.loads(infor_user.text)
        tasks_true = json.loads(tasks_complete.text)
        tasks = json.loads(tasks.text)

        id_user = str(user_name.get('id'))

        result = {id_user: []}
        for task in tasks:
            result[id_user].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user_name.get('username')
            })

        name_file = '{}.json'.format(user_name.get('id'))

        with open(name_file, 'w') as json_file:
            json.dump(result, json_file)

    else:
        print("Not user with this value")
