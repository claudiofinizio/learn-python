import logging
import unittest
import yaml
from pprint import pprint

import app

filepath = 'config.yaml'
filepath = '_config.yaml'


logging.basicConfig(
    level="INFO",
    format='[%(asctime)-10s] [%(levelname)8s] %(name)s: %(message)s',
    datefmt="%Y-%m-%d@%H:%M:%S",
    filename="logs.txt",
    filemode="w+"
)

class MissingConfigFile(Exception):
    pass


class CorruptedConfigFile(Exception):
    pass


def sample_function(filepath):
    logger = logging.getLogger(__name__)
    logger.info("filepath is {}".format(filepath))

    try:
        with open(filepath) as infile:
            try:
                stream = yaml.load(infile)
            except yaml.YAMLError as err:
                logger.info("config file is corrupted", exc_info=True)
                raise CorruptedConfigFile
            else:
                return stream
    except IOError as err:
        print 'must log file is missing'
        logger.info("config file is missing", exc_info=True)
        raise MissingConfigFile(err)


if __name__ == "__main__":

    # First, log from this module.
    try:
        data = sample_function(filepath)
    except MissingConfigFile:
        print 'handle missing'
    except CorruptedConfigFile:
        print 'handle corrupted'
    else:
        pprint(data)
    finally:
        pass

    # Next, log from another module.
    print 'code still running :-D'
    runner = unittest.TextTestRunner()
    test_suite = app.suite()
    runner.run(test_suite)