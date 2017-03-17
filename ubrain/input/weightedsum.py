from functools import reduce

from .inputfunc import InputFunc


class WeightedSum(InputFunc):

    def __init__(self):
        self._output = 0.0

    def calculate(self, input_connections):
        super(WeightedSum, self).calculate(input_connections)
        func = (lambda acc, connection: acc + connection.weight * connection.src.output)
        self._output = reduce(func, input_connections, 0.0)

    @property
    def output(self):
        return self._output
