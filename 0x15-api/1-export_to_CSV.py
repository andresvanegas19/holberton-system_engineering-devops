#!/usr/bin/python3
""" Is a script that make a request to save into csv """

import csv
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
        ).json()

        # to print the task
        tasks_true = requests.get(
            '{}todos?userId={}&completed=true'.format(url, user_id)
        ).json()

        # the whole tasks
        tasks = requests.get(
            '{}todos?userId={}'.format(url, user_id)
        ).json()

        row_list = []

        for task in tasks:
            row_list.append(
                [
                    user_id,
                    user_name.get('username'),
                    task.get('completed'),
                    task.get('title')
                ])

        csv.register_dialect(
            'design',
            delimiter=',',
            quoting=csv.QUOTE_ALL,
            quotechar='"'
        )

        name_file = '{}.csv'.format(user_id)
        with open(name_file, 'w', newline='') as file:
            writer = csv.writer(file, dialect='design')
            writer.writerows(row_list)

    else:
        print("Not user with this value")
