"""
A interceptor which maintains a log
"""

from interceptor import Interceptor
import logging

logging.basicConfig(
        filename="app_log.txt", 
        format="[%(asctime)s] %(message)s", 
        datefmt="%d-%m-%Y %H:%M:%S",
        level=logging.INFO)

class LoggingInterceptor(Interceptor):

    def execute(self, request):
        print("Inside the logging interceptor")
        logging.info(f"Executing request - {request}")

        # request should be a class and provide an API for the conc interceptor