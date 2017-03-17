from .inputfunc import InputFunc
from functools import reduce


class Sum(InputFunc):

    def __init__(self):
        self._output = 0.0

    def calculate(self, input_connections):
        super(Sum, self).calculate(input_connections)
        func = (lambda acc, connection: acc + connection.src.output)
        self._output = reduce(func, input_connections, 0.0)

    @property
    def output(self):
        return self._output
