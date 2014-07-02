from pyramid.view import view_config
import pyramid_web_app.data.database


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):

    # Lots of logic / db access / whatever here.

    return dict(project='Deutsche Bank Web App', feature='Show off')
    #return {'project': 'Deutsche Bank Web App', '':''}


@view_config(route_name='all_posts', renderer='templates/posts.pt')
def posts_view(request):

    # Lots of logic / db access / whatever here.
    posts = pyramid_web_app.data.database.DataBase.posts

    return dict(posts=posts)

