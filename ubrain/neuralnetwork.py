import json
from .layer import Layer


class NeuralNetwork:
    def __init__(self, conf_str, encoding):
        conf = json.loads(conf_str, encoding)
        self._layers = list()

    def append_layer(self, layer):
        """Add a layer at the end of this network.

        :param layer: The new layer to add.
        """
        if not isinstance(layer, Layer):
            raise TypeError("a Layer is required")

        self._layer.append(layer)

    def insert_layer(self, index, layer):
        """Inserts a layer at the specified position in this network.

        :param index: Index of the layer before witch to insert.
        :param layer: The new layer to insert.
        """
        if not isinstance(index, int):
            raise TypeError("an int is required")

        if 0 > index > len(self._layers):
            raise IndexError("index out of range")

        if not isinstance(layer, Layer):
            raise TypeError("a Layer is required")

        self._layers.insert(index, layer)

    def pop_layer(self, index):
        """Removes layer at the specified position in this network and returns it.

        :param index: Index of the layer to remove.
        :return The removed layer.
        """
        if len(self._layers) is 0:
            raise IndexError("pop from empty network")

        if not isinstance(index, int):
            raise TypeError("a int is required")

        if 0 > index > len(self._layers):
            raise IndexError("index out of range")

        return self._layers.pop(index)