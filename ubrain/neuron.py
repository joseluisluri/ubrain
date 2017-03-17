# coding=UTF8
import ubrain.input.inputfunc as infunc
import ubrain.input.weightedsum as wsum
import ubrain.trans.step as step
import ubrain.trans.transferfunc as trfunc
import ubrain.weight as weight


class Neuron:
    """Basic unit in an artificial neural network. This model uses the McCulloch-Pitts (MCP) representation. The neuron
    can receive one or more inputs (dendrites) and produce an output (axon) using a function (InputFunc). This value is
    passed to a non-linear function (TransferFunc) inspired to build logic gates.
    """

    def __init__(self, label="", error=0.0, bias=weight.Weight(0.0), input_func=wsum.WeightedSum(),
                 transfer_func=step.Step()):
        """Create an instance of a artificial neuron.

        :param str label: The label for this neuron. Default: "".
        :param float error: The error for this neuron. Default: 0.0.
        :param ubrain.weight.Weight bias: The bias for this neuron. Default weight: 0.0.
        :param ubrain.input.inputfunc.InputFunc input_func: The input function for this neuron. Default: \
        ubrain.input.weightedsum.WeightedSum.
        :param ubrain.trans.transferfunc.TransferFunc transfer_func: The transfer function for this neuron. Default: \
        ubrain.trans.step.Step.
        """
        if not isinstance(label, str):
            raise TypeError("a str is required")
        elif not isinstance(error, float):
            raise TypeError("a float is required")
        elif not isinstance(bias, weight.Weight):
            raise TypeError("a Weight is required")
        elif not isinstance(input_func, infunc.InputFunc):
            raise TypeError("input_func must be a subclass of InputFunc")
        elif not isinstance(transfer_func, trfunc.TransferFunc):
            TypeError("transfer_func must be a subclass of TransferFunc")
        else:
            self._label = label
            self._error = error
            self._bias = bias
            self._input_conn = set()
            self._output_conn = set()
            self._input_func = input_func
            self._transfer_func = transfer_func

    @property
    def error(self):
        """The error for this neuron. The error rate is typically the proportion of deviation from the expected
        value.

        :getter: Returns the error for this neuron.
        :setter: Sets the error for this neuron.
        :type: float
        """
        return self._error

    @error.setter
    def error(self, error):
        if not isinstance(error, float):
            raise TypeError("a float is required")
        elif not 0.0 <= error <= 1.0:
            raise ValueError("exceptions must be between 0.0 and 1.0")
        else:
            self._error = error

    @property
    def bias(self):
        """The bias for this neuron. A bias node provides flexibility to a neural network model as it allows you to
        change the input function, which can be critical to successful learning.

        :getter: Returns the bias for this neuron.
        :setter: Sets the bias for this neuron.
        :type: ubrain.weight.Weight
        """
        return self._bias

    @bias.setter
    def bias(self, bias):
        if not isinstance(bias, weight.Weight):
            raise TypeError("a Weight is required")
        else:
            self._bias = bias

    @property
    def label(self):
        """The label for this neuron. A label is used to identify neurons on a form-to provide a description.

        :getter: Returns the label for this neuron.
        :setter: Sets the label for this neuron.
        :type: str
        """
        return self._label

    @label.setter
    def label(self, label):
        if not isinstance(label, str):
            raise TypeError("a str is required")
        else:
            self._label = label

    @property
    def input_func(self):
        """The input function for this neuron.

        :getter: Returns the input function for this neuron.
        :setter: Sets the input function for this neuron.
        :type: ubrain.input.inputfunc.InputFunc
        """
        return self._input_func

    @input_func.setter
    def input_func(self, input_func):
        if not isinstance(input_func, infunc.InputFunc):
            raise TypeError("input_func must be a subclass of InputFunc")
        else:
            self._input_func = input_func

    @property
    def transfer_func(self):
        """The transfer function for this neuron.

        :getter: Returns the transfer function for this neuron.
        :setter: Sets the transfer function for this neuron.
        :type: ubrain.trans.transferfunc.TransferFunc.
        """
        return self._transfer_func

    @transfer_func.setter
    def transfer_func(self, transfer_func):
        if not isinstance(transfer_func, trfunc.TransferFunc):
            raise TypeError("transfer_func must be a subclass of TransferFunc")
        else:
            self._transfer_func = transfer_func

    @property
    def input_conn(self):
        """Set of input connections fot his neuron.

        :getter: Returns a set (copy) of input connections for this neuron.
        :rtype: {ubrain.connection.Connection}
        """
        return self._input_conn.copy()

    @property
    def output_conn(self):
        """Set of output connections fot his neuron.

        :getter: Returns a set (copy) of output connections form this neuron.
        :rtype: {ubrain.connection.Connection}
        """
        return self._output_conn.copy()

    @property
    def output(self):
        """The last value calculated for this neuron.

        :getter: Returns the last value calculated for this neuron.
        :rtype: float
        """
        return self._transfer_func.output

    def calculate(self):
        """Calculates neuron's output."""
        self._input_func.calculate(self._input_conn)
        self._transfer_func.calculate(self._input_func.output)
