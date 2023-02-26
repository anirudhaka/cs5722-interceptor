"""
the base dispatcher
"""

from abc import ABC, abstractmethod

class AbstractDispatcher(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def register_interceptor(self):
        pass

    @abstractmethod
    def remove_interceptor(self):
        pass

    @abstractmethod
    def notify(self):
        pass

class Dispatcher(AbstractDispatcher):
    def __init__(self, context_object=None) -> None:
        self.context_object = context_object
        self.interceptors = set()

    def register_interceptor(self, interceptor):
        self.interceptors.add(interceptor)

    def remove_interceptor(self, interceptor):
        self.interceptors.remove(interceptor)

    def notify(self, context_object):
        self.context_object = context_object
        for interceptor in self.interceptors:
            interceptor.update(context_object)