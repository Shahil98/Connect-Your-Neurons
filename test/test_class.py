#!/usr/bin/env python3

import sys
sys.path.insert(0, "../")
from Flask_App.main import create_keras_model


class TestClass:

    def test_one(self):

        test_dict = {
            "number_of_layers": "3",
            "optimizer": "Adam",
            "loss_function": "Binary CrossEntropy",
            "layers": [{"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}]
        }
        model_test = create_keras_model(test_dict)
        assert model_test == test_dict

    def test_two(self):

        test_dict = {
            "number_of_layers": "3",
            "optimizer": "Adam",
            "loss_function": "Binary CrossEntropy",
            "layers": [{"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}]
        }
        model_test = create_keras_model(test_dict)
        assert model_test == test_dict

    def test_three(self):

        test_dict = {
            "number_of_layers": "3",
            "optimizer": "Adam",
            "loss_function": "Binary CrossEntropy",
            "layers": [{"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}]
        }
        model_test = create_keras_model(test_dict)
        assert model_test == test_dict
