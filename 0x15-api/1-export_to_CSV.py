#!/usr/bin/python3
"""Gather data from API"""
import requests
import sys

if __name__ == "__main__":

    ID = sys.argv[1]
    site = 'https://jsonplaceholder.typicode.com/'
    dos = requests.get(site + 'todos?userId={}'.format(ID)).json()
    user = requests.get(site + 'users/{}'.format(ID))
    name = user.json().get('username')
    with open('{}.csv'.format(ID), 'w') as export:
        for i in dos:
            export.write('"{}","{}","{}","{}"\n'.format(ID, name,
                                                           i['completed'],
                                                           i['title']))
