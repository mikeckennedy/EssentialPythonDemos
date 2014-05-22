import datetime

import pyramid.httpexceptions
import pyramid.response
import pyramid_handlers

from blog_app.controllers.base import BaseController
import blog_app.data.data_layer
from blog_app.data.data_layer import Post
from blog_app.data.data_layer import DB


class PostController(BaseController):
    @pyramid_handlers.action(renderer="blog_app:templates/blog/list.pt")
    def list(self):
        ordered_posts = blog_app.data.data_layer.DB.all_posts
        ordered_posts.sort(key=lambda p: p.published)
        ordered_posts.reverse()
        return dict(posts=ordered_posts)

    def show(self):
        the_id = int(self.data['id'])
        post = blog_app.data.data_layer.DB.find_post_by_id(the_id)
        return pyramid.response.Response("would show " + post.title)

    @pyramid_handlers.action(
        name='create',
        renderer="blog_app:templates/blog/create.pt",
        request_method="GET")
    def create_get(self):
        print('get')
        return {}

    @pyramid_handlers.action(
        name='create',
        renderer="blog_app:templates/blog/create.pt",
        request_method="POST")
    def create_post(self):
        pub = datetime.datetime.now()
        content = self.data['content']
        title = self.data['title']
        p = Post(4, title, pub, content)
        DB.all_posts.append(p)

        return pyramid.httpexceptions.HTTPFound('/posts')


