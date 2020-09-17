#!/usr/bin/python3
"""
An script to request the information about reddit and make statisct
"""
import requests

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'andressantiagore@gmail.com',
}


def top_ten(subreddit):
    """ This function will return the most 10 top post from reddit
    it not return nothing"""
    url = 'https://www.reddit.com/r/{}/top/.json?limit=10'.format(subreddit)
    r = requests.get(url=url, headers=headers, allow_redirects=False)
    if r.status_code == 302:
        print("None")
        return None
    posts = r.json()

    if not posts.get("data").get("children"):
        print("None")
        return None
    for dictionary in posts.get("data").get("children"):
        print(dictionary.get('data').get('title'))
