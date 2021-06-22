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

    def get_var_name(self, var):
        # Following only works in 3.8+, eat error if thrown
        try:
            var_name = f"{var=}".split("=")[0]
            return var_name
        except Exception as e:
            return type(var)

class DictFormatter(Formatter):

    def format(self, unformatted, indent=3):
        formatted = dumps(unformatted, indent=indent)
        return formatted


class ListFormatter(Formatter):

    def format(self, unformatted):
        string_list = [f"|{i}|{el}|" for i, el in enumerate(unformatted)]
        var_name = self.get_var_name(unformatted)
        f"\n".join([var_name] + string_list)