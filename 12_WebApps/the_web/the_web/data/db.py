class DB:
    posts = None

    @classmethod
    def all_posts(cls):
        if DB.posts is not None:
            return DB.posts

        DB.posts = []
        DB.posts.append(Post("First post", "This is the first!!", 1))
        DB.posts.append(Post("Another post", "This is the second!!", 2))
        return DB.posts

    @classmethod
    def find_post(cls, post_id):
        for p in DB.all_posts():
            if p.id == post_id:
                return p


class Post:
    def __init__(self, title, text, id):
        self.id = id
        self.text = text
        self.title = title