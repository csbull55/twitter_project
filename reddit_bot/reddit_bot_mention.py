# Christian Bull

"""
this will hopefully be the final mention bot
replies to mentions with reply_word
this utilizes the inbox.stream() method, manages unread and read replys
"""

import praw
import emoji


# creates instance off credentials in praw file
reddit = praw.Reddit('bot1',
                     user_agent='bot1 user agent',
                     )

