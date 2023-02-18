"""
The client code
"""

from application import Application
from basic_interceptor import BasicInterceptor

def main():
    interceptor = BasicInterceptor(Application())
    interceptor.execute("request")

if __name__ == "__main__":
    main()