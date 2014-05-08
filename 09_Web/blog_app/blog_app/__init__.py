from pyramid.config import Configurator
from blog_app.controllers.home import HomeController
from blog_app.controllers.posts import PostController


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
    config.add_static_view('static', 'static', cache_max_age=3600)
    #config.add_route('home', '/')
    #config.add_route('home_blog_list', '/blog')

    config.add_handler('home_index', '/', handler=HomeController, action="index")

    config.add_handler('posts_general', '/posts/{action}/{id}', handler=PostController)
    config.add_handler('posts_general2', '/posts/{action}', handler=PostController)
    config.add_handler('posts_general3', '/posts', handler=PostController, action="list")


    config.scan()
    return config.make_wsgi_app()
