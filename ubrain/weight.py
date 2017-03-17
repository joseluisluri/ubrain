# coding=UTF8
import random


class Weight:
    """Neuron connection weight entity."""

    def __init__(self, value=0.0):
        """Create an instance of a weight connection with the specified value.

        :param value: The weight value in range [0, 1]. Default: 0.0.
        """
        if not isinstance(value, float):
            raise TypeError("a float is required")

        if 0 <= value <= 1:
            self._value = value
            self._previous_value = 0.0
        else:
            raise ValueError("weight must be between 0 and 1")

    @property
    def value(self):
        """Returns the current weight value."""
        return self._value

    @value.setter
    def value(self, value):
        """Sets the weight value.

        :param value: The weight value in range [0, 1]. Default: 0.0.
        """
        if not isinstance(value, float):
            raise TypeError("a float is required")

        if 0 <= value <= 1:
            self._previous_value = self._value
            self._value = value
        else:
            raise ValueError("weight must be between 0 and 1")

    @property
    def previous_value(self):
        """Returns the previous weight value."""
        return self._previous_value

    def randomize(self):
        """Sets random weight value in range [0, 1]."""
        self.value = random.random()
