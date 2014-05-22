import pyramid.response
import pyramid_handlers
from blog_app.controllers.base import BaseController


class HomeController(BaseController):
    @pyramid_handlers.action(renderer="blog_app:templates/home/index.pt")
    def index(self):
        return {'project': "Blog app"}