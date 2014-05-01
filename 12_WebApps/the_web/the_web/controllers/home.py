import pyramid_handlers
from the_web.controllers.base import BaseController


class HomeController(BaseController):


    @pyramid_handlers.action(renderer='the_web:templates/home/index.pt')
    def index(self):
        return {'project': 'Home: ESRI Web 2.0'}
