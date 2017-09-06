# -*- coding: utf-8 -*-


def decorator_(func):
    def func_wrapper(*args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        """
        LEARN THIS (IMPORTANTE): la firma di func_wrapper DEVE essere 
        (*args, **kwargs) e non solamente **kwargs. Questo perché il "self"
        passato dal metodo della classe (i.e.: del_record(self)) è un metodo
        posizionale, non un keyword-argument. Si dice infatti che in un 
        metodo di istanza il primo parametro è l'istanza (e la si chiama self)
        mentre in un metodo definito con 'classmethod' il primo parametro
        posizionale è la classe.
        """
        return func(*args, **kwargs)
    return func_wrapper


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