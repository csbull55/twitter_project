# Christian Bull
# python3.7

"""
this is the main file for the reddit bot
basic tasks is it will reply to comments that meet a certain parameter
in the subs that are specified in the subs file
"""

import praw
from subs_crawl import subs_to_crawl


def sub_obj(sub):
    subreddit_lookup = reddit.subreddit(sub)
    posts = [submission.title for submission in subreddit_lookup.hot(limit=5)]
    return posts


# creates instance off credentials in praw file
reddit = praw.Reddit('bot1',
                     user_agent='bot1 user agent',
                     )

# returns top posts from subreddits
for sub in subs_to_crawl():
    posts = sub_obj(sub)
    print(sub + '\n' + '\n'.join(posts) + '\n')
