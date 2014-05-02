import datetime
import json

from pyramid.response import Response
from pyramid.view import view_config


posts = [
    dict(title='Post 1', pub=str(datetime.datetime(2014, 4, 1))),
    dict(title='Post 2', pub=str(datetime.datetime(2014, 4, 5))),
]


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'rest_py'}

@view_config(route_name='api_posts', request_method='GET')
def get_posts(request):
    return Response(json_body=posts)

@view_config(route_name='api_posts', request_method='POST')
def add_posts(request):
    new_post = request.json_body
    posts.append(new_post)
    return Response('CREATED OK', status=201)
















