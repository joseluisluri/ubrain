# coding=UTF8
import math
from .transferfunc import TransferFunc


class Sigmoid(TransferFunc):
    def __init__(self, slope=1.0):
        assert isinstance(slope, float)
        self._slope = slope
        self._output = 0.0

    @property
    def slope(self):
        return self._slope

    @slope.setter
    def slope(self, slope):
        assert isinstance(slope, float)
        self._slope = slope

    @property
    def output(self):
        return self._output

    def calculate(self, value):
        super(Sigmoid, self).calculate(value)
        self._output = 1 / (1 + math.e ^ (-self._slope * value))
