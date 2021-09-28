#!/usr/bin/python3
"""Get data from an API"""
import json
import requests


def top_ten(subreddit):
    """Shows top ten post"""
    url = "https://www.reddit.com/r/{}/.json?limit=10".format(subreddit)
    headers = {'User-Agent': "requested"}

    response = requests.get(url, headers=headers)
    if response.status_code in [302, 404]:
        print('None')
    else:
        posts = response.json()['data']['children']
        for top in posts:
            print(top['data']['title'])
