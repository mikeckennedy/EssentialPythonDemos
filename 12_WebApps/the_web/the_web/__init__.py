from pyramid.config import Configurator
from the_web.controllers.home import HomeController
from the_web.controllers.posts import PostsController


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
    config.add_static_view('static', 'static', cache_max_age=3600)
    # config.add_route('home', '/')
    # config.add_route('home_2', '/no_place_like_home/{home_town}')

    config.add_handler('home', '/',
	handler=HomeController, action='index')

    config.add_handler('posts_home_noslash', '/posts',
	handler=PostsController, action='index')
    config.add_handler('posts_home', '/posts/',
	handler=PostsController, action='all')

    config.add_handler('posts_act', '/posts/{action}', handler=PostsController)

    config.add_handler('posts_id', '/posts/{action}/{id}',
	     handler=PostsController)



    config.scan()
    return config.make_wsgi_app()
