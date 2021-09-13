#!/usr/bin/python3
"""Gather data from API"""
import requests
import sys

if __name__ == "__main__":

    count = 0
    total = 0

    ID = sys.argv[1]
    site = 'https://jsonplaceholder.typicode.com/'
    dos = requests.get(site + 'todos?userId={}'.format(ID)).json()
    for i in dos:
        total = total + 1
        if i['completed'] is True:
            count = count + 1
    user = requests.get(site + 'users/{}'.format(ID))
    name = user.json().get('name')
    print('Employee {} is done with tasks({}/{}):'.format(name, count, total))
    for i in dos:
        if i['completed'] is True:
            print('\t {}'.format(i['title']))
