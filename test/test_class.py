#!/usr/bin/env python3

import sys
sys.path.insert(0, "../")
from code.main import create_keras_model


class TestClass:

    def test_one(self):

        test_dict = {
            "number_of_layers": "3",
            "optimizer": "Adam",
            "loss_function": "Binary CrossEntropy",
            "layers": [{"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}]
        }
        model_test = create_keras_model(test_dict)
        for i in range(len(test_dict["layers"])):
            assert int(test_dict["layers"][i]["number_of_neurons"]) == model_test["config"]["layers"][i]["config"]["units"]
            assert test_dict["layers"][i]["activation"].lower() == model_test["config"]["layers"][i]["config"]["activation"]

    def test_two(self):

        test_dict = {
            "number_of_layers": "3",
            "optimizer": "Adam",
            "loss_function": "Binary CrossEntropy",
            "layers": [{"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}]
        }
        model_test = create_keras_model(test_dict)
        for i in range(len(test_dict["layers"])):
            assert int(test_dict["layers"][i]["number_of_neurons"]) == model_test["config"]["layers"][i]["config"]["units"]
            assert test_dict["layers"][i]["activation"].lower() == model_test["config"]["layers"][i]["config"]["activation"]

    def test_three(self):

        test_dict = {
            "number_of_layers": "3",
            "optimizer": "Adam",
            "loss_function": "Binary CrossEntropy",
            "layers": [{"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}]
        }
        model_test = create_keras_model(test_dict)
        for i in range(len(test_dict["layers"])):
            assert int(test_dict["layers"][i]["number_of_neurons"]) == model_test["config"]["layers"][i]["config"]["units"]
            assert test_dict["layers"][i]["activation"].lower() == model_test["config"]["layers"][i]["config"]["activation"]