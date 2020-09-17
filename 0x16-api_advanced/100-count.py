#!/usr/bin/python3
"""
An script to request the information about reddit and make statisct
"""
import requests

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'andressantiagore@gmail.com',
}


def requested(url, hot_list=[], next_page=None):
    """This the function that will return a list of request"""
    url = '{}&after={}'.format(url, next_page)
    r = requests.get(url=url, headers=headers, allow_redirects=False)
    if r.status_code == 302:
        print('status')
        return None
    posts = r.json()
    if not posts.get("data").get("children"):
        return None

    hot_list.append(
        posts.get('data').get('children')[0].get('data').get('title')
    )

    return requested(url, hot_list, posts.get('data').get('after'))


def count_words(subreddit, word_list=[]):
    """ This function will return the most 10 top post from reddit
    it not return nothing"""
    url = 'https://www.reddit.com/r/{}/top.json?limit=1&count=1' \
        .format(subreddit)
    r = requests.get(url=url, headers=headers, allow_redirects=False)
    if r.status_code == 302:
        return None
    posts = r.json()
    if posts.get('error') == 404 or not posts.get("data").get("children"):
        return None

    word_list.append(
        posts.get('data').get('children')[0].get('data').get('title')
    )
    requested(url, word_list, posts.get('data').get('after'))
    return word_list

