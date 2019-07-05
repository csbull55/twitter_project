"""
this bot replies to mentions
it's extremely simple as it only monitors it's inbox, so it can be used on any sub
"""

import time
import pickle
import praw
import emoji

# creates instance off credentials in praw file
reddit = praw.Reddit('bot1',
                     user_agent='bot1 user agent',
                     )

# tries to open list of mentions, creates new list if not
try:
    file_object = open('mention_ids.pydata', 'rb')
    reply_ids = pickle.load(file_object)
    file_object.close()
except:
    reply_ids = []


# defines parameters
emoji = emoji.emojize(':crab:', use_aliases=True) * 3
reply_word = ('{} $11 {}'.format(emoji, emoji))

# every x amount of time, reply to new mentions
while True:
    for mention in reddit.inbox.mentions(limit=25):
        if mention.id not in reply_ids and mention.un:
            mention.reply(reply_word)
            reply_ids.append(mention.id)

            # stores reply_ids in list
            try:
                file_object = open('mention_ids.pydata', 'wb')
                pickle.dump(reply_ids, file_object)
                file_object.close()
            except Exception as e:
                print(e)
    time.sleep(30)
