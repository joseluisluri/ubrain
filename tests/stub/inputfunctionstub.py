import ubrain.input.inputfunc as infunc


class InputFunctionStub(infunc.InputFunc):

    def __init__(self, output=0.0):
        self._output = output

    @property
    def output(self):
        return self._output

    def calculate(self, input_connections):
        pass
