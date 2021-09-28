#!/usr/bin/python3
"""Gets data from an API"""
import json
import requests


def top_ten(subreddit):
    """Shows top ten post"""
    url = 'https://www.reddit.com/r/{}/top.json?limit=10'.format(subreddit)
    agent = {'User-Agent': 'requested'}
    response = requests.get(url, headers=agent)
    if response.status_code in [302, 404]:
        print('None')
    elif response.status_code == '200':
        posts = response.json()['data']['children']
        for top in posts:
            print(top['data']['title'])
