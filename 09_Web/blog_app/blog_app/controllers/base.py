

class BaseController:
    def __init__(self, request):
        self.request = request
        self.data = dict()
        self.init_matches()

    def init_matches(self):
        for key in self.request.matchdict:
            self.data[key] = self.request.matchdict[key]
        for key in self.request.GET:
            self.data[key] = self.request.GET[key]
        for key in self.request.POST:
            self.data[key] = self.request.POST[key]

