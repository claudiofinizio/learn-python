#!/usr/bin/python

# -*- coding: utf-8 -*-
def lazyprop(fn):
    attr_name = '_lazy_' + fn.__name__
    @property
    def _lazyprop(self):
        if not hasattr(self, attr_name):
            #print '\n\t\t--- @ _lazyprop looking for', attr_name, '--- Setting the cache...\n'
            setattr(self, attr_name, fn(self))
        #print '\n\t\t--- @ _lazyprop now cached for', attr_name, '---\n'
        return getattr(self, attr_name)
    return _lazyprop
 



class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]




class Cane(object):
    __metaclass__ = Singleton

    def __init__(self, nome):
        print '*****operazione costosa: (fatta una volta per tutte) lettura del database o del file...*****'
        self._nome = nome

    @lazyprop
    def abbaia(self):
        print '\t### operazione minore (tipo calcolo) (comunque fatta una volta per tutte)###'
        print self._nome.upper()


def test_singletons():
    fido = Cane('Pallino')
    fido.abbaia
    print 'grosso'
    fido = Cane('Dodo')
    fido.abbaia


if __name__ == '__main__':
    test_singletons()