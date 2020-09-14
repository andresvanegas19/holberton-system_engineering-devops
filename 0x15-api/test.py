#!/usr/bin/python3
""" Is a script that make a request to JSON """

import requests

url = 'https://jsonplaceholder.typicode.com/'

# to get the user name
infor_user = requests.get('{}users'.format(url)).json()

print(infor_user)

