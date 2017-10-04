import logging
import yaml
from pprint import pprint

filepath = 'config.yaml'
filepath = '_config.yaml'


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
                print 'YAML corrotto'
                raise CorruptedConfigFile
            else:
                return stream
    except IOError:
        print 'manca il file'
        # QUESTO raise CORRISPONDE A UN reraise E DI CONSEGUENZA
        # NEL BLOCCO <if __name__ == "__main__"> LA <except IOError> VIENE
        # CHIAMATA.
        raise


if __name__ == "__main__":
    try:
        data = sample_function(filepath)
    except IOError:
        print 'must log missing'
        print 'must handle missing'
    except CorruptedConfigFile:
        print 'must log corrupted'
        print 'must handle corrupted'
    else:
        pprint(data)
    finally:
        pass
