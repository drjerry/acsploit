VALUE = 'value'
DESCRIPTION = 'description'


class Options(object):
    def __init__(self):
        self._options = {}

    def __getitem__(self, key):
        return self.get_value(key)

    def __setitem__(self, key, value):
        if key not in self._options:
            raise KeyError('add_option() must be used to add new options')
        self.set_value(key, value)

    def add_option(self, name, default_value, description):
        if type(name) is not str:
            raise TypeError('Option name must be a string, not a %s' % str(type(name)))
        if name in self._options:
            raise KeyError('Cannot add duplicate option %s' % name)
        self._options[name] = {VALUE: default_value,
                               DESCRIPTION: description}

    def get_option_names(self):
        return self._options.keys()

    def get_value(self, name):
        return self._options[name][VALUE]

    def set_value(self, name, value):
        # type conversions for non-str values
        if type(self._options[name][VALUE]) is bool:
            value = value in [True, 'True', 'true', 'Yes', 'yes', 'Y', 'y']
        if type(self._options[name][VALUE]) is int:
            value = int(value)
        self._options[name][VALUE] = value

    def get_description(self, name):
        return self._options[name][DESCRIPTION]
