from django.http import Http404
import json

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        # print("before request")
        response = self.get_response(request)
        # print("after request\n\n\n")
        # print(request)
        # print(request.build_absolute_uri())
        # print("after request\n\n\n")

        # Code to be executed for each request/response after
        # the view is called.
        #raise Http404("The link seems to be broken")
        return response