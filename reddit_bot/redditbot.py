# Christian Bull
# python3.7

"""
this is the main file for the reddit bot
basic tasks is it will reply to comments that meet a certain parameter
in the subs that are specified in the subs file
"""

import time
import praw
import emoji
from subs_crawl import subs_to_crawl


# class for each sub
class Subobj():
    def __init__(self, sub, num_of_post):
        self.sub = sub
        self.num_of_post = num_of_post
        self.subobj = reddit.subreddit(self.sub)

    # grabs post obj from hot post, used in other functions
    def sub_posts(self):
        posts = [submission for submission in self.subobj.hot(limit=self.num_of_post)]
        return posts

    def post_titles(self):
        titles = [submission.title for submission in self.sub_posts()]
        return titles

# main
# creates instance off credentials in praw file
reddit = praw.Reddit('bot1',
                     user_agent='bot1 user agent',
                     )

# creates sub to crawl instance, limits to front page, creates list of post objects
new_sub = Subobj(subs_to_crawl()[0], 25)
posts = new_sub.sub_posts()

# empty word dict to count the word, sets word and reply word
word = 'crab_emoji'
reply_word = emoji.emojize(':crab:', use_aliases=True)
num_of_crabs = {word: 0}

# loads more comments after "load more", limit is set to 2 to for memory purposes
posts[0].comments.replace_more(limit=2)

# crawls the comment, if comment has word, reply with reply_word
for comment in posts[0].comments.list():
    if word in comment.body:
        num_of_crabs[word] += 1
        comment.reply(reply_word)





