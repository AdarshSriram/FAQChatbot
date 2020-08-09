import praw
from praw.models import MoreComments
import pandas as pd
import json
import csv
import config

corpus = dict()
output_file = 'conglomerate.csv'
posts_limit = 1000


reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent,
                     username=config.username,
                     password=config.password)

topics_dict = {"title": [],
               "score": [],
               "id": [], "url": [],
               "comms_num": [],
               "created": [],
               "body": []}

data_dict = {"context": [],
             "text response": []}

subreddit_list = [reddit.subreddit('Cornell'), reddit.subreddit(
    'CsMajors'), reddit.subreddit('college')]

top_subreddit_list = []
for i in subreddit_list:
    top_subreddit_list.append(i.hot(limit=posts_limit))

with open('../corpora/%s' % output_file, mode='w') as csv_file:
    fieldnames = ['context', 'text response']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for top_subreddit in top_subreddit_list:
        for submission in top_subreddit:
            submission.comment_sort = 'best'
            submission.comment_limit = 1
            for top_level_comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                    continue
                writer.writerow({'context': submission.title,
                                 'text response': top_level_comment.body})
