#!/usr/bin/python3
"""
An script to request the information about reddit and make statisct
"""
import requests
import sys

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'andressantiagore@gmail.com',
}

url = 'https://www.reddit.com/r/{}/about.json'.format(sys.argv[1])
r = requests.get(url=url, headers=headers, allow_redirects=False)
print(r.status_code == 302)
