from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import session, Post, Comment, engine
import pandas as pd
import psycopg2

import praw
from praw.models import MoreComments
import config


def scrape():
    reddit = praw.Reddit(client_id=data[config.client_id],
                         client_secret=data[config.client_secret],
                         user_agent=data[config.user_agent],
                         username=data[config.username],
                         password=data[config.password])

    LIMIT = 5000

    subreddit_list = [reddit.subreddit('Cornell'), reddit.subreddit('college')]
    top_subreddit_list = []
    for i in subreddit_list:
        top_subreddit_list.append(i.hot(limit=LIMIT))

    fieldnames = ['context', 'text response']

    for top_subreddit in top_subreddit_list:
        for submission in top_subreddit:
            submission.comment_sort = 'best'
            submission.comment_limit = 3
            for comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                    continue
                post = Post(post_id=submission.id,
                            link=submission.url, text=submission.title)
                comm = Comment(comment_id=comment.id,
                               link=comment.url, text=comment.body, post=submission.id)
                try:
                    session.add(post)
                    session.add(comm)

                except Exception as e:
                    session.rollback()
                    print(f'Error occured while adding to db: {e}')

    session.commit()


def to_df():
    df = pd.read_sql_table(table_name='posts', con='sqlite:///corpus.db')
    return df


if __name__ == '__main__':
    scrape()
