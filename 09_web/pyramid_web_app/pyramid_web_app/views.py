import json

import pyramid.response
from pyramid.view import view_config

import pyramid_web_app.data.database


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    # Lots of logic / db access / whatever here.

    return dict(project='Deutsche Bank Web App', feature='Show off')
    # return {'project': 'Deutsche Bank Web App', '':''}


@view_config(route_name='all_posts', renderer='templates/posts.pt')
def posts_view(request):
    # Lots of logic / db access / whatever here.
    posts = pyramid_web_app.data.database.DataBase.posts

    return dict(posts=posts)


@view_config(route_name='api_list', request_method="GET")
def api_all_posts(request):
    data = pyramid_web_app.data.database.DataBase.posts
    return pyramid.response.Response(json_body=data)

    #return pyramid.response.Response(json.dumps(data))
    #return pyramid.response.Response("LISTED\!")


@view_config(route_name='api_list', request_method="POST")
def api_create_post(request):
    new_post = request.json_body
    pyramid_web_app.data.database.DataBase.posts.append(new_post)
    return pyramid.response.Response("CREATED!", status=201)

