import ubrain.weight as weight


class WeightStub(weight.Weight):
    def __init__(self, value=0.0, previous_value=0.0, randomize=0.0):
        self._value = value
        self._previous_value = previous_value
        self._randomize = randomize

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def previous_value(self):
        return self._previous_value

    @previous_value.setter
    def previous_value(self, value):
        self._previous_value = value

    @property
    def randomize(self):
        return self._randomize

    @randomize.setter
    def randomize(self, value):
        self._randomize = value
