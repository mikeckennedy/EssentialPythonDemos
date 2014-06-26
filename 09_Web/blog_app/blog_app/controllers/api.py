import pyramid.response
import pyramid_handlers

from blog_app.controllers import BaseController
import blog_app.data
import blog_app.data.data_layer


class PostsAPIController(BaseController):
    @pyramid_handlers.action()
    def all_posts(self):
        all_posts = [
            p.__dict__
            for p in blog_app.data.DB.all_posts
        ]
        return pyramid.response.Response(json_body=all_posts)
        # return pyramid.response.Response(json.dumps(all_posts))

    @pyramid_handlers.action()
    def show(self):
        if not 'id' in self.request.matchdict:
            print("ID not passed to method")
            return pyramid.response.Response(status=404, body="No found")

        id_text = self.request.matchdict['id']
        if id_text is None or len(id_text.strip()) == 0:
            print("Id not well formed")
            return pyramid.response.Response(status=404, body="No found")

        post_id = int(id_text)

        post = blog_app.data.DB.find_post_by_id(post_id)
        if post is None:
            return pyramid.response.Response(status=404, body="No found")
        return pyramid.response.Response(json_body=post.__dict__)

    # @pyramid_handlers.action()
    # def posts(self):
    #     id_text = self.request.matchdict['id']
    #
    #     post_id = int(id_text)
    #     post = blog_app.data.DB.find_post_by_id(post_id)
    #
    #     return pyramid.response.Response(json_body=post.__dict__)


    @pyramid_handlers.action(name='create', request_method='GET')
    def create_get(self):
        return pyramid.response.Response("Please post you blog entry to this url..")


    @pyramid_handlers.action(name='create', request_method='POST')
    def create_post(self):
        # create the post
        data = self.request.json_body
        p = blog_app.data.data_layer.Post(4, data['title'], data['published'], data['content'])

        blog_app.data.DB.all_posts.append(p)
        return pyramid.response.Response("CREATED SUCCESSFULLY", status=201)

    def details(self, post_id):
        return None


    def details(self, post_id):
        return None

