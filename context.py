"""
defines all the context objects
"""
from abc import ABC, abstractmethod
from datetime import datetime

class Context(ABC):
    def __init__(self) -> None:
        self.created_at = None
        self.data = None

    @abstractmethod
    def __str__(self):
        print("Base context object")

    @abstractmethod
    def get_creation_time(self):
        pass

class CustomerContext(Context):
    def __init__(self, customer_object) -> None:
        self.created_at = datetime.now().replace(microsecond=0).isoformat()
        self.customer_object = customer_object

    def __str__(self):
        return f"Context object for the customer: {self.customer_object.get_name()}"

    def get_creation_time(self):
        return self.created_at

    def get_customer_name(self) -> str:
        return self.customer_object.get_name()

    def get_statement(self):
        return self.customer_object.statement()

