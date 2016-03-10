import logging
import os
from config import APPDIR

def get_logger(name):
    return CustomLogger(name).logger

class CustomLogger(logging.Logger):

    LOGGING_DIR = os.path.join(APPDIR, 'logs')
    CONSOLE_DEFAULT_LEVEL = logging.DEBUG
    CONSOLE_FORMAT = '[\033[1;34m%(name)s\033[0m] %(message)s'
    FILE_DEFAULT_LEVEL = logging.DEBUG

    def __init__(self, name, level=CONSOLE_DEFAULT_LEVEL, logfile=''):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logfile = logfile
            self.console_level = level
            self._set_handlers()

    def _set_handlers(self):
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setFormatter(ConsoleFormatter(CustomLogger.CONSOLE_FORMAT))
        ch.setLevel(self.console_level)
        self.logger.addHandler(ch)
        if self.logfile:
            fh = logging.FileHandler(os.path.join(APPDIR, LOGGING_DIR, self.logfile))
            fh.setLevel(FILE_DEFAULT_LEVEL)
            self.logger.addHandler(fh)

class ConsoleFormatter(logging.Formatter):

    COLOR_HASH = {
            logging.ERROR:'1;31m',
            logging.WARN:'1;33m',
            logging.DEBUG:'38;5;247m'
        }

    def __init__(self, msg):
        logging.Formatter.__init__(self, msg)

    def format(self, record):
        # if record.levelname == 'ERROR':
        #     record.msg = '\033[1;31m'+str(record.msg)+'\033[0m'
        # elif record.levelname == 'DEBUG':
        #     record.msg = '\033[38;5;247m'+str(record.msg)+'\033[0m'
        if record.levelno in ConsoleFormatter.COLOR_HASH.keys():
            record.msg = '\033[{color}{msg}\033[0m'.format(color=ConsoleFormatter.COLOR_HASH[record.levelno], msg=str(record.msg))
        return logging.Formatter.format(self, record)
