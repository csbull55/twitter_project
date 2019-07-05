"""
this will be for more advanced testing of functions
I don't imagine that this project will get too complex
but I want to start getting into the habit of structuring projects
correctly from the start
instead of getting too deep and having to restructure
"""

import praw
import emoji
from subs_crawl import subs_to_crawl

# creates instance off credentials in praw file
reddit = praw.Reddit('bot1',
                     user_agent='bot1 user agent',
                     )

word ='crab_emoji'
reply_word = emoji.emojize(':crab:', use_aliases=True)

for sub in subs_to_crawl():
    for comment in reddit.subreddit(sub).stream.comments():
        if word in comment.body:
            comment.reply(reply_word * 3)
            print('replied to {}'.format(comment.body))