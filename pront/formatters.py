"""Everything related to formatting"""
from abc import ABC, abstractmethod
from json import dumps


class Formatter():

    def format(self, unformatted, indent: int = 3):
        """Basic formatting done here, collection specific
            go in implementations

        :param unformatted: variable to print
        :type unformatted: any
        :param indent: number of spaces to indent, defaults to 3
        :type indent: int, optional
        :return: formatted var
        :rtype: str
        """
        var_type = self.get_var_type(unformatted)
        j = dumps(unformatted, indent=indent)
        formatted = f"{var_type}\n{j}"
        return formatted

    def get_var_type(self, var):
        return f"Type: <{type(var).__name__}>"
