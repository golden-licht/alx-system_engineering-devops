#!/usr/bin/python3
"""
Contains a recursive function that queries the reddit api,
parses the title of all hot articles, and prints a sorted count of
given keywords (case-insensitive, delimited by spaces)
"""
import requests


def count_words(subreddit, word_list, after='', count=0, dictionary={}):
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'user-agent': 'my-app/0.0.1'}
    payload = {'after': after, 'count': count}

    response = requests.get(
        url,
        headers=headers,
        params=payload,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json()['data']
    children = data['children']
    for child in children:
        title = child['data']['title'].lower()
        count_words_from_string(word_list, title, dictionary)
        count += 1

    after = data['after']
    if after is None:
        print_dict_sorted_by_value(dictionary)
    else:
        return count_words(subreddit, word_list, after, count, dictionary)


def count_words_from_string(word_list, string, dictionary):
    word_set = set(word_list)

    for word in word_set:
        count = sum(word == item for item in string.split())
        if word in dictionary:
            dictionary[word] += count
        elif count != 0:  # if word is new but it has non zero count
            dictionary[word] = count


def print_dict_sorted_by_value(dictionary):
    list = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    for value in list:
        print(f'{value[0]}: {value[1]}')
