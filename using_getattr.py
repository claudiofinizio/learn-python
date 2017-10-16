class Uno(object):
    pass


class Due(object):
    pass


class Tre(object):
    def __getattr__(self, item):
        value = True
        setattr(self, item, value)
        return value


class Quattro(object):
    def __getattr__(self, item):
        value = False
        setattr(self, item, value)
        return value


class Cinque(object):
    # Here we use __getattr__ for several attributes, which arewhose default
    # values are grouped in the variable <dispatcher>.
    def __getattr__(self, item):
        dispatcher = {
            'has_this': False,
            'age': 20
            'football': 'Juve'
        }
        value = dispatcher.get(item, False)
        setattr(self, item, value)
        return value


uno = Uno()

# This will raise an error because "has_this" was never assigned to "uno".
try:
    if uno.has_this:
        print 'abbiente'
    else:
        print 'poveromo'
except AttributeError as err:
    print "uno has no <has_this> property defined."

due = Due()
due.has_this = True
# This will not raise any error because "has_this" was assigned to "due"
# in the row above.
if due.has_this:
    print 'abbiente'
else:
    print 'poveromo'


tre= Tre()
# This will return 'abbiente' since, even if "has_this" was not assigned to
# "tre", still the __getattr__ will set its value to "True" and return it.
if tre.has_this:
    print 'abbiente'
else:
    print 'poveromo'

quattro = Quattro()
# This will return 'poveromo' since, even if "has_this" was not assigned to
# "tre", still the __getattr__ will set its value to "False" and return it.
if quattro.has_this:
    print 'abbiente'
else:
    print 'poveromo'

cinque = Cinque()
if cinque.has_this:
    print 'abbiente'
else:
    print 'poveromo'
if cinque.age > 20:
    print 'adulto'
else:
    print 'adolescente'
if cinque.macchiavelli:
    print 'si'
else:
    print 'no'
