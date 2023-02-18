"""
Manages interceptors and calls application code
"""

class InterceptorManagerDispatcher:
    def __init__(self, application) -> None:
        self.application = application
        self.interceptors = set()

    def add(self, interceptor) -> None:
        """
        add/register an interceptor
        """
        self.interceptors.add(interceptor)

    def remove(self, interceptor) -> None:
        """
        remove an interceptor
        """
        self.interceptors.remove(interceptor)

    def execute(self, request) -> None:
        """
        execute the request
        """
        for interceptor in self.interceptors:
            interceptor.execute(request)
        self.application.execute(request)