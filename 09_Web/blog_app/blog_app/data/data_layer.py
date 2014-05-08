import datetime


class Post:
    def __init__(self, title, published, content):
        self.content = content
        self.published = published
        self.title = title

class DB():
    all_posts = [
        Post("First post", datetime.datetime.now(), "CONTENT"),
        Post("Second post", datetime.datetime.now(), "CONTENT"),
        Post("Third post", datetime.datetime.now(), "CONTENT")
    ]