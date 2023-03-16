import abc


class Parent(abc.ABC):
    @abc.abstractmethod
    def get_info(self, parameter):
        """Get parameter info"""

    @abc.abstractmethod
    def set_info(self, parameter, value):
        """Set parameter to value"""


class Child(Parent):

    def __init__(self):
        self._parameters = {}

    def get_info(self, parameter):
        return self._parameters.get(parameter)

    def set_info(self, parameter, value):
        self._parameters[parameter] = value
        return print(self._parameters)


c1 = Child()
c1.set_info('name', 'BB-8')
