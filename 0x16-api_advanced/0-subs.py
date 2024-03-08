#!/usr/bin/python3
"""
    Uses Reddit API for printing number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Getting the number of subscriberst
    """
    myurl = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'request'}
    Myresponse = requests.get(myurl, headers=headers, allow_redirects=False)

    if Myresponse.status_code != 200:
        return 0

    data = Myresponse.json().get("data")
    subs = data.get("subscribers")

    return subs
