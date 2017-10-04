import yaml
from pprint import pprint

filepath = '_config.yaml'
filepath = 'config.yaml'

"""
with open(filepath) as infile:
    stream = yaml.load(infile)
"""


try:
    infile = open(filepath)
except IOError:
    print 'manca il file'
else:
    try:
        stream = yaml.load(infile)
    except yaml.YAMLError:
        print 'YAML corrotto'
    else:
        pprint(stream)
    finally:
        infile.close()
