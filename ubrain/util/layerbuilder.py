from ..layer import Layer
from ..neuron import Neuron
from ..input.weightedsum import InputFunc, WeightedSum
from ..trans.step import TransferFunc, Step


class LayerBuilder:

    def __init__(self):
        self._label = ""
        self._size = 0
        self._input_function = WeightedSum
        self._transfer_function = Step

    def label(self, label):
        if not isinstance(label, str):
            raise TypeError("a str is required")

        self._label = label
        return self

    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("an int is required")

        if size < 0:
            raise ValueError("size must be equal or higher than 0")

        self._size = size
        return self

    def input_function(self, input_function):
        if not isinstance(input_function, InputFunc):
            raise TypeError("input_func must be a subclass of InputFunction")

        self._input_function = input_function
        return self

    def transfer_function(self, transfer_function):
        if not isinstance(transfer_function, TransferFunc):
            raise TypeError("input_func must be a subclass of InputFunction")

        self._transfer_function = transfer_function
        return self

    def build(self):
        layer = Layer()
        layer.label = self._label

        is_multi_input_func = isinstance(self._input_function, list)
        is_multi_transfer_func = isinstance(self._transfer_function, list)

        if is_multi_input_func and len(self._input_function) != self._size \
                or is_multi_transfer_func and len(self._transfer_function) != self._size:
            raise TypeError("size of lists must be equal than {0]}".format(self._size))

        for i in range(self._size):
            layer.append(Neuron(
                label="{0}.{1}".format(self._label, i),
                input_func=self._input_function[i] if is_multi_input_func else self._input_function,
                transfer_func=self._transfer_function[i] if is_multi_transfer_func else self._transfer_function))
        return layer
