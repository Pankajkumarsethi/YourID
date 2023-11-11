import logging
from logging.handlers import TimedRotatingFileHandler


class Logger:
    # create logger

    @staticmethod
    def logGen():

        logLevel = logging.DEBUG
        logger = logging.getLogger("YourID")
        fh = TimedRotatingFileHandler(".\\logs\\automation.log", when="w6", backupCount=12)
        logger.setLevel(logLevel)
        fh.setLevel(logLevel)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logLevel)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch and fh
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # add ch and fh to logger
        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger

