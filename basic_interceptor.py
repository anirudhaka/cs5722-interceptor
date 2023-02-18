"""
A basic Interceptor
"""

class BasicInterceptor:
    def __init__(self, application) -> None:
        self.application = application

    def execute(self, request):
        print("Inside the interceptor.")
        self.application.execute(request)