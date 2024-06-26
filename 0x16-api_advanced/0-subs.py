#!/usr/bin/python3
"""returns the number of subscribers from a sub redit"""


import json
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers in a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "lesuudaAPI"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    try:
        results = response.json().get("data")
        return results.get("subscribers")
    except json.decoder.JSONDecodeError:
        return 0
    return 0
