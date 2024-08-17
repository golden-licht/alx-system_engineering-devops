#!/usr/bin/python3
"""
Contains a function that queries the reddit api and prints
the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?count=0&limit=10'
    headers = {'user-agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        children = response.json()['data']['children']
        for child in children:
            print(child['data']['title'])
    else:
        print(None)
