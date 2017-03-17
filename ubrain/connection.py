# coding=UTF8
import ubrain.neuron
import ubrain.weight


class Connection:
    """Weighted connection between two neurons. Once it has been created, you can modify the weight associated but not
    the source of destination. However, you can enable/disable the connection or create a new one.
    """

    def __init__(self, src, dest, weight=ubrain.weight.Weight()):
        """Creates an instance of a new connection between two neurons with the specified weight.

        :param ubrain.neuron.Neuron src: The source neuron for this connection.
        :param ubrain.neuron.Neuron dest: The destination neuron for this connection.
        :param ubrain.weight.Weight weight: The weight associated to this connection.

        .. note:: When a connection is created, it is associated to each neuron.

        .. code-block:: python
           :linenos:

            >>> import ...
            >>> a = Neuron()
            >>> b = Neuron()
            >>> a.output_conn # {}
            >>> b.input_conn # {}
            >>> c = Connection(a, b) # <__main__.Connection object at 0x00F50F10>
            >>> a.output_conn # {<__main__.Connection object at 0x00F50F10>}
            >>> b.input_conn # {<__main__.Connection object at 0x00F50F10>}
        """
        if not isinstance(src, ubrain.neuron.Neuron):
            raise TypeError("an ubrain.neuron.Neuron is required")
        elif not isinstance(dest, ubrain.neuron.Neuron):
            raise TypeError("an ubrain.neuron.Neuron is required")
        elif not isinstance(weight, ubrain.weight.Weight):
            raise TypeError("an ubrain.weight.Weight is required")
        elif src is dest:
            raise ValueError("a connection must be between two different neurons")
        else:
            self._src = src
            self._dest = dest
            self._weight = weight
            self.enabled = True

    @property
    def src(self):
        """The source neuron from this connection.

        :getter: Returns the source neuron.
        :rtype: ubrain.neuron.Neuron
        """
        return self._src

    @property
    def dest(self):
        """The destination neuron from this connection.

        :getter: Return the destination neuron.
        :rtype: ubrain.neuron.Neuron
        """
        return self._dest

    @property
    def weight(self):
        """The weight associated to this connection.

        :getter: Returns the weight for this connection.
        :setter: Sets the weight for this connection.
        :type: ubrain.weight.Weight
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        if not isinstance(weight, ubrain.weight.Weight):
            raise TypeError("an ubrain.weight.Weight is required")
        else:
            self._weight = weight

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        if not isinstance(enabled, bool):
            raise TypeError("a bool is required")
        elif enabled:
            self._src._output_conn.add(self)
            self._dest._input_conn.add(self)
        else:
            self._src._output_conn.remove(self)
            self._dest._input_conn.remove(self)

        self._enabled = enabled

    def __hash__(self):
        return hash(repr(self))
