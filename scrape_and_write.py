import praw
import os
import docx
import re

base_dir = "/home/jcanso/nosleep/"

if not os.path.isdir(base_dir):
    os.mkdir(base_dir)


reddit = praw.Reddit(client_id='PUT_YOURS_HERE', client_secret="PUT_YOURS_HERE", user_agent="PUT_YOURS_HERE", username="PUT_YOURS_HERE", password="PUT_YOURS_HERE")

subreddit = reddit.subreddit('nosleep')

latest_posts = subreddit.new(limit=20)

for post in latest_posts:
    """
    print(post.title)
    print("==========")
    print(post.selftext)
    print("\r\n")
    """
    mutilated_title = re.sub('[\.\'\"]', '', post.title)

    file_name = base_dir + mutilated_title.replace(" ", "_") + ".docx"
    file_name = file_name.encode('ascii', 'ignore')
    file_name = file_name.decode()
    print(file_name)

    file = docx.Document()

    file.add_heading(post.title, 0)

    post_body = file.add_paragraph(post.selftext)

    file.save(file_name)
