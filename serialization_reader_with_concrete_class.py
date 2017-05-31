#!/usr/bin/python

# -*- coding: utf-8 -*-

# Python standard libraries
import yaml
import json
import os
import logging

from .. main.metaclasses import Singleton
from . decorators import unpack_serialization
from . exceptions import (
    YAMLFileIsCorrupted,
    JSONFileIsCorrupted,
)


class ReaderMetaclass(type):
    @property
    @unpack_serialization
    def read_yaml(cls):
        if getattr(cls, '_READ_YAML', None) is None:
            logging.info('costly database call executing...')
            with open(os.path.join(cls.config_filepath, 'rules.yaml'), 'r') as stream:
                try:
                    information = yaml.load(stream)
                    logging.debug(information)
                except yaml.YAMLError as err:
                    logging.error('YAMLFileIsCorrupted', exc_info=True)
                    raise YAMLFileIsCorrupted
                else:
                    logging.info('using cached _READ_YAML')
                    cls._READ_YAML = information
        return cls._READ_YAML


class RulesReader(object):
    __metaclass__ = ReaderMetaclass
    __metaclass__ = Singleton

    config_filepath = os.path.join(os.path.dirname(__file__), os.pardir, 'config')

    @classmethod
    def read(cls, config_filename):
        if '.'.join([config_filename, 'yaml']) in os.listdir(cls.config_filepath):
            try:
                configuration = cls.read_yaml
            except YAMLFileIsCorrupted:
                raise IOError('Correggi le regole di parsing nel file "{}" e riavvia l\'applicazione'.format(config_filename))
            else:
                return configuration
        elif 'rules.yaml' in os.listdir(cls.config_filepath):
            logging.info('trying YAML...')
            try:
                configuration = cls.read_json
            except JSONFileIsCorrupted:
                raise IOError('Correggi le regole di parsing nel file "{}" e riavvia l\'applicazione'.format(config_filename))
            else:
                return configuration
        else:
            logging.error('Manca il file di configurazione dell\'SQL', exc_info=True)
            raise IOError('Manca il file di configurazione dell\'SQL')



