#!/usr/bin/python3
"""Gets data from an API"""
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Shows hot post"""
    hot_post = []
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    agent = {'User-Agent': 'requested'}
    parameters = {'after': after, 'limit': '100'}
    response = requests.get(url, headers=agent,
                            params=parameters, allow_redirects=False)
    if response.status_code in [302, 404]:
        return None
    else:
        posts = response.json()['data']['children']
        after = response.json()['data']['after']
        for hot in posts:
            hot_list.append(hot)
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
