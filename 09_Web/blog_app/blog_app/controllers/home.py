import pyramid.response
import pyramid_handlers
from blog_app.controllers.base import BaseController


class HomeController(BaseController):
    @pyramid_handlers.action()
    def index(self):
        return pyramid.response.Response("index")

