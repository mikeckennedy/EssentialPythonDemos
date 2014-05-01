from pyramid.renderers import get_renderer


class BaseController:
    def __init__(self, requests):
        self.requests = requests
        layoutRenderer = get_renderer("the_web:templates/shared/layout.pt")
        self.layout = layoutRenderer.implementation().macros['layout']


