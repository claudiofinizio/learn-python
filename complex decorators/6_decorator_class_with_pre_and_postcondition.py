# -*- coding: utf-8 -*-


def confirm_deletion(func):
    def func_wrapper(*args, **kwargs):

        # args[0] is "self"
        message = args[0]._sentences['confirm']
        choice = raw_input(message)
        if choice == "y":
            func(*args, **kwargs)
        else:
            print 'Nothing done "stop propagation"'

    return func_wrapper


class Recordset(object):
    def __init__(self):
        self._records = range(10)
        self._sentences = {
            'confirm': "Are you sure? y/n"
        }

    @confirm_deletion
    def decorated_deletion(self, index):
        self._records.remove(index)
        print self._records


if __name__ == '__main__':
    rst = Recordset()
    rst.decorated_deletion(index=5)