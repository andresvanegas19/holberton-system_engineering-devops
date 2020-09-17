#!/usr/bin/python3
""" Is a script that make a request to JSON """


import json
import requests
import sys


def find_info_todo(user_id):
    """ This function will search for the id the user and display the
    dreams and list to do """
    url = 'https://jsonplaceholder.typicode.com/'

    # to get the user name
    user_name = requests.get(
        '{}users/{}'.format(url, user_id)
    ).json()

    # the whole tasks
    tasks = requests.get(
        '{}todos?userId={}'.format(url, user_id)
    ).json()

    result = {user_id: []}
    for task in tasks:
        result[user_id].append({
            "username": user_name.get('username'),
            "task": task.get('title'),
            "completed": task.get('completed'),
        })

    return result


if __name__ == "__main__":

    result = {}
    for i in range(1, 11):
        result.update(find_info_todo(str(i)))

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(result, json_file)
