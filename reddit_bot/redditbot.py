# Christian Bull
# python3.7

"""
this is the main file for the reddit bot
basic tasks is it will reply to comments that meet a certain parameter
in the subs that are specified in the subs file
"""

import praw

# creates instance off credentials in praw file
reddit = praw.Reddit('bot1',
                     user_agent='bot1 user agent',
                     )

subreddit_lookup = reddit.subreddit('all')

posts = [submission.title for submission in subreddit_lookup.hot(limit=10)]

print('\n'.join(posts))
