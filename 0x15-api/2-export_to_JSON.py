#!/usr/bin/python3
"""Gather data from API"""
import requests
import sys
import json

if __name__ == "__main__":

    ID = sys.argv[1]
    site = 'https://jsonplaceholder.typicode.com/'
    dos = requests.get(site + 'todos?userId={}'.format(ID)).json()
    user = requests.get(site + 'users/{}'.format(ID))
    name = user.json().get('username')
    form = []
    with open('{}.json'.format(ID), 'w') as export:
        for i in dos:
            task = {'task': i['title'],
                    'completed': i['completed'],
                    'username': name
                    }
            form.append(task)
        info = {ID: form}
        json.dump(info, export)
