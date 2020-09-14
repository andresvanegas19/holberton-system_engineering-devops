#!/usr/bin/python3
""" Is a script that make a request to  """


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
        user_name = requests.get(
            '{}users/{}'.format(url, user_id)
        ).json().get('name')

        # to print the task
        tasks_true = requests.get(
            '{}todos?userId={}&completed=true'.format(url, user_id)
        ).json()

        # the whole tasks
        tasks = requests.get(
            '{}todos?userId={}'.format(url, user_id)
        ).json()

        print('Employee {} is done with tasks({}/{})'.format(
            user_name,
            len(tasks_true),
            len(tasks)))

        for task in tasks_true:
            print("\t {}".format(task.get('title')))

    else:
        print("Not user with this value")
