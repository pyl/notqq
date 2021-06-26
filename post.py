#https://www.jcchouinard.com/post-on-reddit-api-with-python-praw/

import json
import praw
import requests

credentials = 'client_secrets.json'
subrl = ['pythonsandlot', 'nopopularopinions']
title = input("Title (Input * for custom subreddit): ")
if title == '*':
    subrl = []
    while True:
        s = input("Input a subreddit. Input * to stop.")
        if s == '*':
            break
        subrl.append(s)
    title = input("Title: ")
selftext = input("Text: ")

with open(credentials) as f:
    creds = json.load(f)
reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])

for sub in subrl:
    subreddit = reddit.subreddit(sub)
    subreddit.submit(title, selftext=selftext)








