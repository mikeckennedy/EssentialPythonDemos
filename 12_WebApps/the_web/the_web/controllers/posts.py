from pyramid.response import Response
import pyramid_handlers
from the_web.controllers.base import BaseController
from the_web.data.db import DB


class PostsController(BaseController):

    @pyramid_handlers.action(renderer="the_web:templates/posts/index.pt")
    def index(self):
        posts = DB.all_posts()
        print(type(posts))
        return dict(all_posts = posts)

    @pyramid_handlers.action(renderer="the_web:templates/posts/show.pt")
    def show(self):
        post_id = int(self.requests.matchdict['id'])
        post = DB.find_post(post_id)
        return dict(title = post.title)

    @pyramid_handlers.action()
    def something(self):
        return Response("Something was called!!")