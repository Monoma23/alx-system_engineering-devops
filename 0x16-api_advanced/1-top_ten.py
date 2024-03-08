#!/usr/bin/python3
"""
    Using reddit API too get first 10 hot posts
"""
import requests


def hot_ten(subreddit):
    """Getting first 10 hot posts"""
    myurl = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'user-agent': 'request'}
    myresponse = requests.get(myurl, headers=headers, allow_redirects=False)

    if myresponse.status_code != 200:
        print(None)
        return

    mydata = myresponse.json().get("mydata").get("children")
    hotTen = "\n".join(post.get("mydata").get("title") for post in mydata)
    print(hotTen)
