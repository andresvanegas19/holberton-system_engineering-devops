#!/usr/bin/python3
"""
An script to request the information about reddit and make statisct
"""
import requests


def number_of_subscribers(subreddit):
    """ This function the porpouse is to request the information
    of the webpage and give the details of the result
    :return the result"""
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'andressantiagore@gmail.com',
    }

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url=url, headers=headers, allow_redirects=False)
    if r.status_code == 302:
        return 0
    r = r.json()
    if r.get('kind') == 'Listing':
        return 0

    return r.get('data').get('subscribers')
