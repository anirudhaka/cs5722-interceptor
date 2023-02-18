"""
The base interceptor code
"""

class Interceptor:
    def execute(self, request):
        print("Inside the interceptor.")