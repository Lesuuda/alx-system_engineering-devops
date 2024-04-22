#!/usr/bin/python3
"""uses a REST API to return employee's TODO List"""


import sys
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks ({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
