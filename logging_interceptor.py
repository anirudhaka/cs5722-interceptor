"""
A interceptor which maintains a log
"""

from interceptor import Interceptor
from context import Context
import logging

logging.basicConfig(
        filename="app_log.txt", 
        format="[%(asctime)s] %(message)s", 
        datefmt="%d-%m-%Y %H:%M:%S",
        level=logging.INFO)

class LoggingInterceptor(Interceptor):

    def update(self, context: Context):
        if context.get_customer_name().lower() == "neo":
            logging.info("Mr. Anderson, welcome back.")
            return
        logging.info(
            f"Context object created at: {context.get_creation_time()}\nmore details: {str(context)}"
        )

        # request should be a class and provide an API for the conc interceptor