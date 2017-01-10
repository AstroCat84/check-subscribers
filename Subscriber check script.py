import praw

reddit = praw.Reddit(client_id='', client_secret="",
                     password='', user_agent='',
                     username='')

s = reddit.subreddit('SUBREDDIT').subscribers

print(s)
