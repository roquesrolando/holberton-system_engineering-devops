#!/usr/bin/python3
"""Gather data from API"""
import requests
import sys
import json

if __name__ == "__main__":

    info = {}
    site = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(site + 'users').json()
    for x in user:
        ID = x.get('id')
        dos = requests.get(site + 'todos?userId={}'.format(ID)).json()
        name = x.get('username')
        form = []
        for i in dos:
            task = {'task': i['title'],
                    'completed': i['completed'],
                    'username': name
                    }
            form.append(task)
        info[ID] = form
        with open('todo_all_employees.json', 'w') as export:
            json.dump(info, export)
