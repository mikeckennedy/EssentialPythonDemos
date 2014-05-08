import datetime


class Post:
    def __init__(self, post_id, title, published, content):
        self.post_id = post_id
        self.content = content
        self.published = published
        self.title = title

class DB():
    all_posts = [
        Post(1,"First post", datetime.datetime.now(), "CONTENT"),
        Post(2,"Second post", datetime.datetime.now(), "CONTENT"),
        Post(3,"Third post", datetime.datetime.now(), "CONTENT")
    ]

    @staticmethod
    def find_post_by_id(post_id):
        for p in DB.all_posts:
            if p.post_id == post_id:
                return p
        return None