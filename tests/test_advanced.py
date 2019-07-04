"""
this will be for more advanced testing of functions
I don't imagine that this project will get too complex
but I want to start getting into the habit of structuring projects
correctly from the start
instead of getting too deep and having to restructure
"""

import praw
from subs_crawl import subs_to_crawl


class Subobj():
    def __init__(self, sub):
        self.sub = sub


    def sub_obj(self):
        sub_reddit = reddit.subreddit(self.sub)
        return sub_reddit


def sub_obj(sub, num_posts):
    subreddit_lookup = reddit.subreddit(sub)
    posts = [submission for submission in subreddit_lookup.hot(limit=num_posts)]
    return posts


# creates instance off credentials in praw file
reddit = praw.Reddit('bot1',
                     user_agent='bot1 user agent',
                     )

# returns top posts from subreddits
for sub in subs_to_crawl():
    posts = sub_obj(sub, 5)
    titles = [post.title for post in posts]
    print('\n'.join(titles))
