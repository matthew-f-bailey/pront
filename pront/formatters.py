"""Everything related to formatting"""
from abc import ABC, abstractmethod
from json import dumps

class Formatter(ABC):
    """Interface for any and all formatters

    :param ABC: Abstract Base Class
    :type ABC: abc.ABC
    """

    @abstractmethod
    def format(self, unformatted):
        pass
