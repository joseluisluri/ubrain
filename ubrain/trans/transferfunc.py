from abc import ABCMeta, abstractmethod, abstractproperty


class TransferFunc:
    __metaclass__ = ABCMeta

    @abstractproperty
    def output(self):
        pass

    @abstractmethod
    def calculate(self, value):
        assert isinstance(value, float), "a float is required"
        pass
