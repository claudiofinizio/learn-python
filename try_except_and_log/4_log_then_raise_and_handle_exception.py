import logging
import yaml
from pprint import pprint

filepath = '_config.yaml'
filepath = 'config.yaml'


class MissingConfigFile(Exception):
    pass


class CorruptedConfigFile(Exception):
    pass


def sample_function(filepath):
    try:
        with open(filepath) as infile:
            try:
                stream = yaml.load(infile)
            except yaml.YAMLError as err:
                print 'must log file is corrupted'
                raise CorruptedConfigFile
            else:
                return stream
    except IOError as err:
        print 'must log file is missing'
        raise MissingConfigFile(err)


if __name__ == "__main__":
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
