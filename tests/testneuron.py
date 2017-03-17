# coding=UTF8
import unittest
import ubrain.neuron

import tests.stub as stub


class TestNeuron(unittest.TestCase):

    def test_calculate(self):
        transfer_func_output = 3.14
        expected_output = 3.14

        neuron = ubrain.neuron.Neuron()
        neuron.input_func = stub.InputFunctionStub()
        neuron.transfer_func = stub.TransferFunctionStub(transfer_func_output)
        self.assertEqual(neuron.output, expected_output, "neuron output must be %s" % expected_output)
