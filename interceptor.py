"""
The base interceptor code
"""
from abc import ABC, abstractmethod

class Interceptor(ABC):
    @abstractmethod
    def update(self, context):
        pass