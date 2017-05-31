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
    YAMLConfigFileIsCorrupted,
    JSONConfigFileIsCorrupted,
)


class ConfigReader(object):
    config_filepath = os.path.join(os.path.dirname(__file__), '..', 'config')

    @classmethod
    @unpack_serialization
    def read_yaml(cls, config_filename):
        logging.info('qwerty')
        with open(os.path.join(cls.config_filepath, '.'.join([config_filename, 'yaml'])), 'r') as stream:
            try:
                configuration = yaml.load(stream)
            except yaml.YAMLError as e:
                logging.error('YAMLFileIsCorrupted', exc_info=True)
                raise YAMLConfigFileIsCorrupted
            else:
                return configuration

    @classmethod
    @unpack_serialization
    def read_json(cls, config_filename):
        with open(os.path.join(cls.config_filepath, '.'.join([config_filename, 'json'])), 'r') as stream:
            try:
                configuration = json.load(stream)
            except ValueError as e:
                logging.error('JSONFileIsCorrupted', exc_info=True)
                raise JSONConfigFileIsCorrupted
            else:
                return configuration

    @classmethod
    def read_file(cls, config_filename):
        if '.'.join([config_filename, 'json']) in os.listdir(cls.config_filepath):
            logging.info('trying JSON...')
            try:
                configuration = cls.read_json(config_filename)
            except JSONFileIsCorrupted:
                raise IOError('Correggi il file di configurazione "{}" e riavvia l\'applicazione'.format(config_filename))
            else:
                return configuration
        elif '.'.join([config_filename, 'yaml']) in os.listdir(cls.config_filepath):
            try:
                configuration = cls.read_yaml(config_filename)
            except JSONConfigFileIsCorrupted:
                raise IOError('Correggi il file di configurazione "{}" e riavvia l\'applicazione'.format(config_filename))
            else:
                return configuration
        else:
            logging.error('Manca il file di configurazione dell\'SQL', exc_info=True)
            raise IOError('Manca il file di configurazione dell\'SQL')



