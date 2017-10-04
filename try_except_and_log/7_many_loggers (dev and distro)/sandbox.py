#! /usr/bin/python
# -*- coding: utf-8 -*-
# Python standard libraries
import yaml

# Python 3rd-part libraries
import wx

# Project modules
import app
from exceptions_ import (
    CorruptedConfigFile,
    MissingConfigFile,
)
from logging_ import (
    dev_logger,
    dist_logger,
)

# Modules only for debugging
from pprint import pprint


filepath = 'infile.yaml'
filepath = '_infile.yaml'


def sample_function(filepath):
    try:
        with open(filepath) as infile:
            try:
                stream = yaml.load(infile)
            except yaml.YAMLError as err:
                dist_logger.error("config file is corrupted", exc_info=False)
                dev_logger.error("config file is corrupted", exc_info=False)
                raise CorruptedConfigFile
            else:
                return stream
    except IOError as err:
        dist_logger.error("config file is missing", exc_info=False)
        dev_logger.error("config file is missing", exc_info=False)
        raise MissingConfigFile(err)


if __name__ == "__main__":
    # First, log from this module.
    try:
        data = sample_function(filepath)
    except MissingConfigFile:
        dist_logger.warning("handling missing config file", exc_info=False)
        dev_logger.warning("handling missing config file", exc_info=False)
    except CorruptedConfigFile:
        dist_logger.warning("handle corrupted config file", exc_info=False)
        dev_logger.warning("handle corrupted config file", exc_info=False)
    else:
        pprint(data)
    finally:
        pass

    # Next, log from another module.
    print 'code still running :-D'
    app.run_suite()