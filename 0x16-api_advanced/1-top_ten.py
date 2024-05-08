#!/usr/bin/python3
"""returns the top 10 posts from a sub redit"""

import json  # Add missing import statement

import requests


def top_ten(subreddit):
    """returns the number of subscribers in a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "lesuudaAPI"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    children = results.get("children")
    if children is not None:
        [print(c.get("data").get("title")) for c in children]
