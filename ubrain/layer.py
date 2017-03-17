# coding=UTF8
import ubrain.neuron


class Layer:
    """Layer of neurons in a neural network."""

    def __init__(self, label="", neurons=[]):
        """Creates an instance of a layer.

        :param str label: The label for this layer. Default: "".
        :param [ubrain.neuron.Neuron] neurons: List of neurons for this layer. Default: [].
        """
        if not isinstance(label, str):
            raise TypeError("a str is required")
        elif not isinstance(neurons, list):
            raise TypeError("a list is required")
        elif any(not isinstance(e, ubrain.neuron.Neuron) for e in neurons):
            raise TypeError("neurons must be a list of ubrain.neuron.Neuron")
        else:
            self._label = label
            self._neurons = neurons

    @property
    def label(self):
        """The label for this layer. A label is used to identify layers on a form-to provide a description.

        :getter: Returns the label for this layer.
        :setter: Sets the label for this layer.
        :type: str
        """
        return self._label

    @label.setter
    def label(self, label):
        if not isinstance(label, str):
            raise TypeError("a str is required")
        else:
            self._label = label

    def insert(self, index, neuron):
        """Inserts a neuron at the specified position in this layer.

        :param int index: Index of the neuron before witch to insert.
        :param ubrain.neuron.Neuron neuron: The new neuron to insert.
        """
        if not isinstance(neuron, ubrain.neuron.Neuron):
            raise TypeError("an ubrain.neuron.Neuron is required")
        else:
            self._neurons.insert(index, neuron)

    def append(self, neuron):
        """Add a neuron at the end of this layer.

        :param ubrain.neuron.Neuron neuron: The new neuron to add.
        """
        if not isinstance(neuron, ubrain.neuron.Neuron):
            raise TypeError("an ubrain.neuron.Neuron is required")
        else:
            self._neurons.append(neuron)

    def pop(self, index):
        """Removes neuron at the specified position in this layer and returns it.

        :param index: Index of the neuron to remove.
        :return: The removed neuron.
        :rtype: ubrain.neuron.Neuron
        """
        return self.__neurons.pop(index)

    def __getitem__(self, index):
        """:getter: Returns the neuron at the specified position in this layer.

        :setter: Sets the neuron at the specified position in this layer.
        :type: ubrain.neuron.Neuron
        """
        return self._neurons[index]

    def __len__(self):
        """Returns number of neurons in this layer.

        :rtype: int
        """
        return len(self._neurons)

    def calculate(self):
        for neuron in self._neurons:
            neuron.calculate()