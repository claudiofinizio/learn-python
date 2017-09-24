"""
Questa versione ripete due volte lo stesso blocco:
    if self.not_empty_string_test(num):
        if self.integer_test(num):
            if self.positive_integer_test(num):
                return True

sia nel PositiveIntegerValidator che nel VotationOrderValidator
"""

class PyValidator(object):
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


class PositiveIntegerValidator(PyValidator, ValidatorMixin):
    def __init__(self, stringa):
        self.str_ = stringa

    def validate(self):
        """
        Chiamo tre @staticmethod usando <self>
        :return:
        """
        num = self.str_
        if self.not_empty_string_test(num):
            if self.integer_test(num):
                if self.positive_integer_test(num):
                    return True
        return False



class VotationOrderValidator(PyValidator, ValidatorMixin):
    def __init__(self, stringa, recordset):
        self.str_ = stringa
        self.list_ = recordset


    def uniqueness_test(self, num):
        _ = len(self.list_)
        _ = num
        return True

    def validate(self):
        num = self.str_
        if self.not_empty_string_test(num):
            if self.integer_test(num):
                if self.positive_integer_test(num):
                    return self.uniqueness_test(num)
        return False


positive_test = PositiveIntegerValidator(5)
print positive_test.validate()

votation_test = VotationOrderValidator(5, range(10))
print votation_test.validate()