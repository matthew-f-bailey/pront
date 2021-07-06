import logging

from pront.caller_info import Caller


class pront():

    def __init__(self) -> None:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(name)s %(levelname)s: %(message)s',
            datefmt='%d-%b-%y %H:%M:%S'
        )
        self.caller = Caller()
        self.level = None

    def info(self, txt):
        self.level = logging.INFO
        self.log(txt)

    def log(self, txt):
        self.level(txt)

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    caller = Caller()
    logging.info(caller.line_no)
    print(caller.module)

    # Create/find logger for calling module
    logger = logging.getLogger(caller.fullpath)
    print(logger)