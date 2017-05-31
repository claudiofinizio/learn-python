#! /usr/bin/python
# -*- coding: utf-8 -*- 

"""Help on module persistence:

Classes, exceptions and functions that are exported by the module:
CLASSES
    SqlStructure - The bookkeeper of Models' structures.

EXCEPTIONS:
    None.

FUNCTIONS:
    None.
 """

# Python standard libraries
import collections
import os

# Python 3rd-part libraries
import wx
import wx.lib.mixins.listctrl as listmix

# Project modules
from . _temp_open import OpenedConfig
from . commons import (
    Singleton,
)
from . decorators import (
    lazyprop,
    memoize_models_in_app,
    memoize_by_string_kwargs,
)
from .regexes import (
    StandardConfig,
)

# Modules only for debugging
from pprint import pprint


class SqlStructure(object):
    """Represents the bookkeeper of the database structure.

    This class stores the hierarchical structure apps -> models -> fields,
    as inferred from the SQL files.

    This class is a singleton, loaded once for all when easyConfig boots.

    * Public methods:
        - 

    * Instance variables:
        - 
    """

    __metaclass__ = Singleton

    def __init__(self):
        print '*****operazione costosa: (fatta una volta per tutte) lettura del database o del file...*****'
        # Step - Connect to the eV SQl file and parse it.
        origin = StandardConfig()
        # Step - Save parser results into the bookkeeper.
        self._apps_models = origin.apps_models
        self._fields = origin.models_fields

    @lazyprop
    def apps_names(self):
        """Returns the list of Django apps."""

        return self._apps_models.keys()

    def apps(self):
        """Returns the WHAT....
        #TODO: da vedere come lo utilizzi.... il nome scelto è criptico!!
        """

        return self._apps_models

    @memoize_models_in_app
    def app_models(self, app_name):
        """Returns the list of models MA DEI RECORDSET , DELLE STRUTTURE O DEI NOMI ?????
        
        Remark: 
        """
        return self._apps_models[app_name]

    @memoize_by_string_kwargs 
    def model_fields(self, app_name, model_name):
        return self._fields[app_name][model_name]


class Persistence(object):
    def recordsets(self):
        return 'Qui metterò i recordsets'


class CurrentConfig(object):
    #TODO: credo che tuti i metodi in questa classe siano privati
    # e come tali metti il _nome
    """Represents the bookkeeper of the database recordsets.

    This class stores the recordsets inferred from parsing the SQL files.

    This class is a singleton, loaded once for all when easyConfig boots.

    * Public methods:
        - recordset: returns the table recordset.

    * Instance variables:
        - 
    """

    __metaclass__ = Singleton

    def __init__(self):
        origin = StandardConfig()
        self._records = origin.records

    def reload_on_open(self, filename, loading_apps_names):
        opened_data = OpenedConfig(filename=filename)
        # Step - Overwrite.
        for app_name in loading_apps_names:
            self._records[app_name] = opened_data._records[app_name]

    def revert_to_original_config(self):
        origin = StandardConfig()
        self._records = origin.records

    def recordsets(self, app_name, model_name):
        """Returns the table recordset.

        The recordset is returned as a Table object
        DA RINOMINARE RECORDSET, ALTRIMENTI CHI CI CAPISCE!!!!
        The records can be extracted by reading the Recordset.records
        attribute. Recordset.records returns a list of Record objects.
        """
        
        return self._records[app_name][model_name]

    def new_record(self, app_name, model_name, new_record):
        
        self._records[app_name][model_name].append(new_record)

    def new_pk(self, app_name, model_name):
        """Returns a unique numeric primary key for a given Django model.
        
        The method returns the highest pk value (plus one) retrieved
        from the records currently existing.

        Precondition: the code calls this method only for those
        recordset wheich have a numeric primary key.
        This precondition is ensured programmatically.

        Examples: members_category, config_meetingquorum may call this
        method. However, config_admissionfieldsvisibility or 
        config_i18nbase may not call this method.
        """
        
        recordset = self._records[app_name][model_name]
        ids = [int(record['id']) for record in recordset]
        return max(ids) + 1


class Table(object):
    #CREDO SIA TEMPORANEA FRA UNS ALVATAGFGIO E L'ALTRO, UINA ROBA DI TIPO USER SESSION.
    """Bookkeeper of table structure.

    * Class variables:
        - __slots__: enforces the required bookkeeper structure.
    """
    
    __slots__ = ['_app_name', '_model_name', '_fields_names', 'records']

    def __init__(self, app_name, model_name, fields_names):
        """Stores the information for which bookkeeping is required."""

        self._app_name = app_name
        self._model_name = model_name
        self._fields_names = fields_names


class RecordFactory(object):
    # vedi: http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
    def value_type_validator(MYSTERY):
        pass

    @staticmethod
    def create(app_name, model_name, fields_names):
        #TODO: perché passi app_name, model_name?

        def field_descriptor(field_name):
            def getter_factory(field_name):
                def getter(self):
                    return getattr(self, "_{}".format(field_name))
                return getter
            #TODO:DEBUG! la 'self' qui dentro non funziona.
            # Al momento non è un problema perché l'uso dei 
            # descriptors di python è stato sostituito con
            # quello dei validators di wxpython.
            def setter_factory(field_name):
                def setter(self, value):
                    try:
                        pass
                        #tester[field['value_type']]
                    except ValueTypeNotRespected:
                        # notifica l'utente con un rifiuto;  ritorna a wx python
                        pass
                    else:
                        pass
                        # setattr
                    finally:
                        pass
                        # ritorna a wx python, ricarica i records nei widgets
                    return setattr(self, "_{}".format(field_name), value)
                return setter
            return property(getter_factory(field_name), setter_factory(field_name))
        
        attributes = {'__slots__': ["_{}".format(name) for name in fields_names]}
        for name in fields_names:
            attributes[name] = field_descriptor(name)
        return type("Record", (object,), attributes)




    class Client(object):
        """Record object storing client information.

        The record fields are:
            - name: the client's name,
            - pk: a pk used to identify each record and perform CRUD operations.
            - acronym: a text field user to map "bp", "ac" ASK PIERGIORGIO: 
            CAPIRE FINO A DOVE SERVE MAPPARE BP, AC....

        Magic methods:
            - __slots__: defines the record's fields.
        """

        __slots__ = ['pk', 'name', 'acronym']

        def __init__(self, pk, name, acronym):
            """Setter of the record's fields' values."""

            self.pk, self.name, self.acronym = pk, name, acronym

