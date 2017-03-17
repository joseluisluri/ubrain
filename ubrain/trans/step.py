# coding=UTF8
from .transferfunc import TransferFunc


class Step(TransferFunc):
    """1 if >= 0 ojito"""
    def __init__(self, high=1.0, low=0.0):
        assert isinstance(high, float), "a float is required"
        assert isinstance(low, float), "a float is required"
        self._high = high
        self._low = low
        self._output = 0.0

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, high):
        assert isinstance(high, float), "a float is required"
        self._high = high

    @property
    def low(self):
        return self._high

    @low.setter
    def low(self, low):
        assert isinstance(low, float), "a float is required"
        self.low = low

    @property
    def output(self):
        return self._output

    def calculate(self, value):
        super(Step, self).calculate(value)
        self._output = self._high if value >= 0.0 else self._low
