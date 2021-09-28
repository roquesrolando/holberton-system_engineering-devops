#!/usr/bin/python3
"""Gets data from an API"""
import json
import requests


def number_of_subscribers(subreddit):
    """Shows number of subscriber"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = {'User-Agent': 'requested'}
    response = requests.get(url, headers=agent)
    if response.status_code in [302, 404]:
        return 0
    return response.json()['data']['subscribers']
