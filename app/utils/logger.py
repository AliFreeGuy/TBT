import logging
import os

class CustomFormatter(logging.Formatter):
    RED = '\x1b[1;91m'
    GREEN = '\x1b[1;92m'
    YELLOW = '\x1b[1;93m'
    CYAN = '\x1b[1;96m'
    NORMAL = '\033[0m'
    FORMAT = "%(levelname)s [%(asctime)s - %(filename)s:%(lineno)d] - %(message)s"

    FORMATS = {
        logging.DEBUG: CYAN + FORMAT + NORMAL,
        logging.INFO: GREEN + FORMAT + NORMAL,
        logging.WARNING: YELLOW + FORMAT + NORMAL,
        logging.ERROR: RED + FORMAT + NORMAL,
        logging.CRITICAL: RED + FORMAT + NORMAL
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

def get_logger():
    logger = logging.getLogger()

    if not os.environ.get('DEBUG'):
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(CustomFormatter())
    logger.addHandler(console_handler)
    
    file_handler = logging.FileHandler('logs.txt')
    file_handler.setFormatter(CustomFormatter())
    logger.addHandler(file_handler)

    return logger

logger = get_logger()
