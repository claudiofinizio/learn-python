import os


# RIPRENDI DA QUI:
# This is a classic Python pitfall. When you define
# http://stackoverflow.com/questions/27629944/python-metaclass-adding-properties
# 
# E POI LEGGI:
# https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
# http://stackoverflow.com/questions/1325673/how-to-add-property-to-a-class-dynamically

# Define one table...
macrocategory = 'config'
model_name = 'config'
# ...its fields...
fields = [
    {'type': 'string', 'name': 'name'},
    {'type': 'bool', 'editable': True, 'name': 'value'},
    {'type': 'color', 'name': 'value_type'}
]
# ...and some sample records.
sample_rows = [
    {   
        'name': 'background subordinate color',
        'value': '#23abd5',
        'value_type': 'color',
    },
    {
        'name': 'superior subordinate color',
        'value': '#fdfd05',
        'value_type': 'color',
    },
]


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Table(object):

    __metaclass__ = Singleton
    __slots__ = ['_macrocategory', '_model_name', '_fields_names', '_records']

    def __init__(self, macrocategory, model_name, fields_names):
        self._macrocategory = macrocategory
        self._model_name = model_name
        self._fields_names = fields_names


class RecordFactory(object):
    # vedi: http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
    def value_type_validator(MYSTERY):
        pass

    @staticmethod
    def create(macrocategory, model_name, fields):

        def descrittore(field):
            def getter_factory(field):
                def getter(self):
                    print 'getter running'
                    return getattr(self, "_{}".format(field['name']))
                return getter

            def setter_factory(field):
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
                    print 'setter running'
                    return setattr(self, "_{}".format(field['name']), value)
                return setter

            return property(getter_factory(field), setter_factory(field))

        attributes = {'__slots__': ["_{}".format(field['name']) for field in fields]}
        for field in fields:
            attributes[field['name']] = descrittore(field)


        return type("Record", (object,), attributes)


def run():
    # Step - Creo la tabella
    fields_names = [field['name'] for field in fields]
    print fields_names
    table = Table(macrocategory=macrocategory, model_name=model_name, fields_names=fields_names)
    # Step - Creo il tipo di record
    Record = RecordFactory.create(macrocategory, model_name, fields)
    print dir(Record), '\n'
    # Popolo i records com i valori di prova (sample_rows)
    records=[]
    for row in sample_rows:
        record = Record()
        print 'record {}:'.format(record)
        for field, value in row.items():
            print '\t* adding {}: {}'.format(field, value)
            setattr(record, field, value)
        print '--end of database row--\n'
        records.append(record)
    # Controllo l'assegnazione, stampando i valori assegnati
    for record in records:
        for field in row:
            test = getattr(record, field)
            print 'checking: {}; retrieved: {}'.format(field, test)
        print '--end of database row--\n'


    # Step - Assegno i record alla tabella

if __name__ == '__main__':
    os.system('clear')
    print '\n'*3,  '=  . '*5, '\n'*5, '\t\t\t\t===== RESTART SHELL ====='
    run()