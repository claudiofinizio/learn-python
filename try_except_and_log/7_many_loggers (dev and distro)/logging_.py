#! /usr/bin/python
# -*- coding: utf-8 -*-
# Python standard libraries
import logging

# Python 3rd-part libraries

# Project modules

# Modules only for debugging
from pprint import pprint


logging.basicConfig(
    level="DEBUG",
    format='[%(asctime)-10s] [%(levelname)8s] %(name)s: %(message)s',
    datefmt="%Y-%m-%d@%H:%M:%S",
    filename="logs.txt",
    filemode="w"
)


# Create loggers.
dev_logger = logging.getLogger('dev' + __name__)
dist_logger = logging.getLogger('dist' + __name__)

# Create handlers.
dev_handler = logging.FileHandler(
    filename="dev_log.log",
    mode="w",
    encoding="UTF-8",
)
dist_handler = logging.FileHandler(
    filename="dist_log.log",
    mode="w",
    encoding="UTF-8",
)

dev_formatter = logging.Formatter(
    fmt="%(name)20s %(message)s",
    datefmt="%Y-%m-%d@%H:%M:%S",
)
dev_handler.setFormatter(dev_formatter)
dist_formatter = logging.Formatter(
    fmt="[%(asctime)10s] %(levelname)-8s %(name)-15s %(message)s",
)
dist_handler.setFormatter(dist_formatter)

dev_logger.setLevel(logging.NOTSET)
dist_logger.setLevel(logging.NOTSET)

# Associate loggers to handlers.
dev_logger.addHandler(dev_handler)
dist_logger.addHandler(dist_handler)


