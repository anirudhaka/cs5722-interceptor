"""
The client code
"""

from application import Application
# from basic_interceptor import BasicInterceptor
from interceptor_manager_dispatcher import InterceptorManagerDispatcher
from logging_interceptor import LoggingInterceptor

def main():
    dispatcher = InterceptorManagerDispatcher(Application())

    log_int = LoggingInterceptor()
    dispatcher.add(log_int)
    dispatcher.execute("test request")

if __name__ == "__main__":
    main()