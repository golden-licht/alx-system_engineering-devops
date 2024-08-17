#!/usr/bin/python3
"""
Contains a function that queries the reddit api and returns
the number of subscribers for a particular subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about/.json'
    headers = {'user-agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
         return response.json()['data']['subscribers']
    else:
        return 0
