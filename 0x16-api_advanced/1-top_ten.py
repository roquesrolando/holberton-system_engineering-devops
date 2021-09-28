#!/usr/bin/python3
"""Gets data from an API"""
import json
import requests


def top_ten(subreddit):
    """Shows top ten post"""
    url = 'https://www.reddit.com/r/{}/top.json?limit=10'.format(subreddit)
    agent = {'User-Agent': 'requested'}
    response = requests.get(url, headers=agent)
    if response.status_code == 200:
        response = response.json().get('data').get('children')

        for post in response:
            title = post.get('data').get('title')
            print(title)
    else:
        print("None")
