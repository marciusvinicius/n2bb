from werkzeug.wrappers import (
    Request,
    Response,
    ResponseStream)
from sommelier.databases.models import possible_filters


class FilterMiddleware():
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        print(">>>>>>>")
        print(request)
        print(dir(request))
        query_params = request.args
        #TODO: Get the filters based on resource
        filters = {
            k:v for k, v in query_params.items() 
                if k in possible_filters
        }

        sort = query_params.get("sort", "").split(",")
        page = query_params.get('page') or 1
        per_page = query_params.get('per_page') or 10

        environ['sort'] = sort
        environ['filters']  = filters
        environ['page']  = {
            'page': int(page),
            'per_page': int(per_page)
        }

        return self.app(environ, start_response)


