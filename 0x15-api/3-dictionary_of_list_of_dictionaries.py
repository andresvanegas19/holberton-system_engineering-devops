#!/usr/bin/python3
""" Is a script that make a request to JSON """

import requests
import json
import csv


def find_info_todo(user_id):
    """ This function will search for the id the user and display the
    dreams and list to do """
    url = 'https://jsonplaceholder.typicode.com/'

    # to get the user name
    user_name = requests.get(
        '{}users/{}'.format(url, user_id)
    ).json()

    # to print the task
    tasks_complete = requests.get(
        '{}todos?userId={}&completed=true'.format(url, user_id)
    )

    # the whole tasks
    tasks = requests.get(
        '{}todos?userId={}'.format(url, user_id)
    )


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


if __name__ == "__main__":
    for i in range(1, 10):
        find_info_todo(i)
