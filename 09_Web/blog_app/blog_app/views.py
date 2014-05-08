import pyramid.response
from pyramid.view import view_config
import blog_app.data.data_layer


# @view_config(route_name='home', renderer='templates/home/index.pt')
# def home_index(request):
#     return {'project': 'The best blog app ever'}
#
# @view_config(route_name='home_blog_list', renderer='templates/blog/list.pt')
# def home_blog_list(request):
#     posts = blog_app.data.data_layer.DB.all_posts
#
#     return dict(posts=[], project="Whateva")
