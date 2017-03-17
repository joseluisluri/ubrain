import ubrain.trans.transferfunc as trfunc


class TransferFunctionStub(trfunc.TransferFunc):

    def __init__(self, output):
        self._output = output

    @property
    def output(self):
        return self._output

    def calculate(self, value):
        pass
