# Christian Bull

"""
this will hopefully be the final mention bot
replies to mentions with reply_word
this utilizes the inbox.stream() method, manages unread and read replys
"""

import pickle
import praw
import emoji


# creates instance off credentials in praw file
reddit = praw.Reddit('bot1',
                     user_agent='bot1 user agent',
                     )

# tries to open list of mentions, creates new list if not
try:
    file_object = open('reply_ids.pydata', 'rb')
    reply_ids = pickle.load(file_object)
    file_object.close()
except:
    reply_ids = []

# defines parameters
reply_parameter = '/u/{}'.format(reddit.user.me())
emoji = emoji.emojize(':crab:', use_aliases=True) * 3
reply_word = ('{} $11 {}'.format(emoji, emoji))

# replies to mentions, saves already replied mentions
while True:
    for item in reddit.inbox.stream():
        if reply_parameter in item.body and item.id not in reply_ids:
            item.reply(reply_word)
            item.mark_read()
            reply_ids.insert(0, item.id)

            # removes old reply.id data
            if len(reply_ids) > 100:
                del reply_ids[-1]

            # stores replied ids
            try:
                file_object = open('reply_ids.pydata', 'wb')
                pickle.dump(reply_ids, file_object)
                file_object.close()
            except Exception as e:
                print(e)
