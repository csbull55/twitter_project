# Christian Bull
# python3.7

"""
this is the main file for the reddit bot
basic tasks is it will reply to comments that meet a certain parameter
in the subs that are specified in the subs file
"""

import praw
from subs_crawl import subs_to_crawl


class Subobj():
    def __init__(self, sub):
        self.sub = sub
        self.subobj = reddit.subreddit(self.sub)


    def sub_posts(self):
        posts = [submission for submission in self.subobj.hot(limit=5)]
        return posts


    def post_titles(self):
        


# creates instance off credentials in praw file
reddit = praw.Reddit('bot1',
                     user_agent='bot1 user agent',
                     )

new_sub = Subobj(subs_to_crawl()[0])

print(new_sub.sub_posts())