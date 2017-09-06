# -*- coding: utf-8 -*-


def with_confirmation_dialog(class_method):
    def func_wrapper(*args, **kwargs):
        message = args[0].message_factory()
        choice = raw_input(message)
        if choice == "y":
            class_method(*args, **kwargs)
        else:
            print 'Nothing done "stop propagation"'
    return func_wrapper


class Recordset(object):
    def __init__(self):
        self._records = range(10)
        self._sentences = {
            'confirm': "Are you sure? y/n"
        }

    def message_factory(self):
        return self._sentences['confirm']

    @with_confirmation_dialog
    def decorated_deletion(self, index):
        self._records.remove(index)
        print self._records


if __name__ == '__main__':
    rst = Recordset()
    rst.decorated_deletion(index=5)