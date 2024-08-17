#!/usr/bin/python3
"""
Contains a recursive function that queries the reddit api
and returns a list containing the titles of
all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    url = f'''https://www.reddit.com/r/
    {subreddit}/hot/.json?after={after}&count={count}'''
    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    print(url)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    children = data['children']
    for child in children:
        hot_list.append(child['data']['title'])
        count += 1

    after = data['after']
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after, count=count)
