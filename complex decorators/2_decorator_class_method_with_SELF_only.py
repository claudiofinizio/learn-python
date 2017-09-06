def decorator_(func):
    def wrapper(self):
        #print 'precondition'
        #print 'execution...'
        #print 'postcondition'
        return func(self)
    return wrapper


class Recordset(object):
    def __init__(self):
        self._records = range(10)
        self._sentences = {
            'confirm': "Are you sure? y/n"
        }

    @decorator_
    def del_record(self):
        index = 5
        message = self._sentences['confirm']
        choice = raw_input(message)
        if choice == "y":
            self._records.remove(index)
            print self._records
        else:
            print 'Nothing done "stop propagation"'


if __name__ == '__main__':
    rst = Recordset()
    rst.del_record()