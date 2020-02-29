import logging
import logging.config


def logger(name):
    logging.config.fileConfig("logger.conf")
    return logging.getLogger(name)
