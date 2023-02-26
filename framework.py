"""
the framework upon which the movie rental application is built
"""

from dispatcher import Dispatcher
from context import Context, CustomerContext
from datetime import datetime

class Framework:
    VERSION = "0.0.1"
    def __init__(self) -> None:
        print(f"##########\nFramework initialised.\nCurrent time: {datetime.now().replace(microsecond=0).isoformat()}\nVersion: {self.VERSION}\n##########")
        self.dispatcher = None
        self.context_object = None

    def event(self):
        """handle an event"""
        self.context = self.create_context()
        self.dispatcher.context_object = self.context

    def create_dispatcher(self, context_obj: Context=None) -> Dispatcher:
        self.dispatcher = Dispatcher(context_obj)
        return self.dispatcher

    def create_context(self):
        self.context_object = Context()
        return self.context_object

    def create_customer_context(self, customer_obj) -> CustomerContext:
        self.context_object = CustomerContext(customer_obj)
        return self.context_object

    