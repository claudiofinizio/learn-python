# -*- coding: utf-8 -*-
"""
Questa versione non ripete più lo stesso blocco,
sia nel PositiveIntegerValidator che nel VotationOrderValidator,
come capitava nel file "1_semplice":
    if self.not_empty_string_test(num):
        if self.integer_test(num):
            if self.positive_integer_test(num):
                return True

Questa versione estrae il blocco di cui sopra in un classmethod.
Dopodiché il classmethod è dispobinile per tutte le classi che
utilizzano il PositiveIntegerValidatorMixin.
"""

class PyValidator(object):
    def __init__(self):
        pass


class ValidatorMixin(object):
    @staticmethod
    def not_empty_string_test(num):
        return True

    @staticmethod
    def integer_test(num):
        return True

    @staticmethod
    def positive_integer_test(num):
        return True


class PositiveIntegerValidatorMixin(ValidatorMixin):

    @classmethod
    def positive_int_validation(cls, num):
        """
        Chiamo tre @staticmethod (da dentro un @classmethod) usando <cls>
        :param num:
        :return:
        """
        if cls.not_empty_string_test(num):
            if cls.integer_test(num):
                if cls.positive_integer_test(num):
                    return True
        return False


class PositiveIntegerValidator(PyValidator, PositiveIntegerValidatorMixin):
    def __init__(self, stringa):
        self.str_ = stringa

    def validate(self):
        """
        Chiamo un @classmethod usando <self>
        :return:
        """
        num = self.str_
        return self.positive_int_validation(num)


class VotationOrderValidator(PyValidator, PositiveIntegerValidatorMixin):
    def __init__(self, stringa, recordset):
        self.str_ = stringa
        self.list_ = recordset

    def uniqueness_test(self, num):
        _ = len(self.list_)
        _ = num
        return True

    def validate(self):
        """
        Chiamo il metodo positive_int_and_uniqueness_validation, ovvero
        un metodo dell'istanza, con il classico <self>.

        :return:
        """
        return self.positive_int_and_uniqueness_validation()

    def positive_int_and_uniqueness_validation(self):
        """
        La mia firma è "self" che si riferisce all'istanza di classe.
        Chiamo il @classmethod "positive_int_validation" usando <self>.
        Chiamo lo @staticmethod "uniqueness_test" usuando ugualmente <self>.
        :param num:
        :return:
        """
        num = self.str_
        if self.positive_int_validation(num):
            return self.uniqueness_test(num)
        return False



positive_test = PositiveIntegerValidator(5)
print positive_test.validate()

votation_test = VotationOrderValidator(5, range(10))
print votation_test.validate()