"""
this bot crawls every comment in a subreddit and replies
this is a framework that allows for a dynamic word and reply
"""

import praw
import emoji
from subs_crawl import subs_to_crawl

# creates instance off credentials in praw file
reddit = praw.Reddit('bot1',
                     user_agent='bot1 user agent',
                     )

replied_comments = []
word = str(reddit.user.me())
reply_word = emoji.emojize(':crab:', use_aliases=True)

for sub in subs_to_crawl():
    for comment in reddit.subreddit(sub).stream.comments():
        if word in comment.body:
            if comment.id not in replied_comments:
                comment.reply(reply_word * 3)
                replied_comments.append(comment.id)
                print(replied_comments)

