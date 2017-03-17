from abc import ABCMeta, abstractmethod, abstractproperty
import ubrain.connection


class InputFunc:
    __metaclass__ = ABCMeta

    @abstractproperty
    def output(self):
        pass

    @abstractmethod
    def calculate(self, input_connections):
        assert any(not isinstance(e, ubrain.connection.Connection) for e in input_connections),\
            "input_conn must be a list of Connection"
        pass
