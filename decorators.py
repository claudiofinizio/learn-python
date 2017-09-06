import collections


def lazyprop(func):
    """Caches the class method return value.

    Stores the result returned by a class instance's method the first time
    the method is invoked, and returns the cached value at every subsequent call.

    Used to decorate persistence.SqlStructure.apps_names.
    """

    attr_name = '_lazy_' + func.__name__

    @property
    def _lazyprop(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)
    return _lazyprop


def memoize_models_in_app(func):
    """Caches the list of models names inside an app.

    Used to decorate persistence.SqlStructure.apps_models.

    * Arguments:
        - the decorated function accepts the Django app's name as argument.
    """

    memo={}

    def helper(self, app_name):
        if app_name not in memo:
            memo[app_name] = func(self, app_name)
        return memo[app_name]
    return helper


def memoize_by_string_kwargs(func):
    """Caches class methods whose kwargs reference hashable types.

    Here used to decorate those methods whose signature includes strings,
    typically app_name, model_name.
    """

    memo={}

    def helper(self, **kwargs):
        hash_ = hash(str(kwargs))
        if hash_ not in memo:
            memo[hash_] = func(self, **kwargs)
        return memo[hash_]
    return helper


class Singleton(type):
    """Singleton boilerplate.

    Every class which shall be a Singleton, inherits from this one.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SqlStructure(object):
    """Represents the bookkeeper of the database structure.

    This class stores the hierarchical structure apps -> models -> fields,
    as inferred from the SQL files.

    This class is a singleton, loaded once for all when easyConfig boots.

    * Public methods:
        -

    * Instance variables:
        -
    """

    __metaclass__ = Singleton

    def __init__(self):
        self._apps_models = {
            'config': ['init', 'config', 'configkind', 'meetingquorum', 'votationquorum', 'meetingvalue', 'csvfield'],
            'reports': ['report', 'rquery', 'rparams', 'routput'],
            'members': ['category'],
            'stations': ['prefix', 'site', 'station']
        }

        self._fields = collections.defaultdict(
            lambda: collections.defaultdict(list))
        self._fields['votations']['anagvotvalue'] = [
            'id',
            'record_title',
            'timestamp_save',
        ]
        self._fields['directions']['monitor_monitor_votation'] = [
            'id',
            'monitor_id',
            'monitorvotation_id',
        ]
        self._fields['directions']['monitorvotation_votationvalue'] = [
            'id',
            'monitorvotation_id',
            'votationvalue_id',
        ]

    @memoize_models_in_app
    def app_models(self, app_name):
        """Returns the list of models MA DEI RECORDSET , DELLE STRUTTURE O DEI NOMI ?????

        Remark:
        """

        return self._apps_models[app_name]

    @memoize_by_string_kwargs
    def model_fields(self, app_name, model_name):
        return self._fields[app_name][model_name]


if __name__ == "__main__":
    sql_structure = SqlStructure()
