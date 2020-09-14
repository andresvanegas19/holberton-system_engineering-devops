#!/usr/bin/python3
""" Is a script that make a request to JSON """

import requests
import sys
import json
import csv


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

        user_name = json.loads(infor_user.text).get('name')
        tasks_true = json.loads(tasks_complete.text)
        tasks = json.loads(tasks.text)

        print('Employee {} is done with tasks({}/{})'.format(
            user_name,
            len(tasks_true),
            len(tasks)))

        for task in tasks_true:
            print("\t {}".format(task.get('title')))

    else:
        print("Not user with this value")
