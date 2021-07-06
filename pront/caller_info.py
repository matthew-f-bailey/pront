import inspect

class Caller():

    def __init__(self) -> None:
        """Creates custom info on calling module
        """
        stack = inspect.stack()[2]
        self._fullpath = stack.filename

        self._line_no = stack.lineno
        self._module = stack.filename.split('\\')[-1].replace(".py", "")

    @property
    def line_no(self):
        return self._line_no

    @property
    def module(self):
        return self._module

    @property
    def fullpath(self):
        return self._fullpath
