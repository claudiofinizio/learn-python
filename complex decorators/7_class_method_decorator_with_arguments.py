# -*- coding: utf-8 -*-


def decorator_(func):
    def func_wrapper(*args, **kwargs):
        print 'indice vale', kwargs['index']
        return func(*args, **kwargs)
    return func_wrapper


def with_confirmation_request(message):
    def confirm_deletion(func):
        def func_wrapper(*args, **kwargs):
            choice = raw_input(message)
            if choice == "y":
                func(*args, **kwargs)
            else:
                print 'Nothing done "stop propagation"'
        return func_wrapper
    return confirm_deletion


class Recordset(object):
    def __init__(self):
        self._records = range(10)
        self._sentences = {
            'confirm': "Are you sure? y/n"
        }

    @decorator_
    def del_record(self, index):
        message = self._sentences['confirm']
        choice = raw_input(message)
        if choice == "y":
            self._records.remove(index)
            print self._records
        else:
            print 'Nothing done "stop propagation"'

    @with_confirmation_request("Are you sure? y/n")
    def decorated_deletion(self, index):
        self._records.remove(index)
        print self._records


if __name__ == '__main__':
    rst = Recordset()
    rst.decorated_deletion(index=5)