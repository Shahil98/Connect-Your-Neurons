import json
from Flask_App.main import createKerasModel, kerasToIr
import tensorflow


class TestClass:

    def test_one(self):

        test_dict = {
            "number_of_layers": "3",
            "optimizer": "Adam",
            "loss_function": "Binary CrossEntropy",
            "layers": [{"number_of_neurons": "513", "activation": "RELU"},
                       {"number_of_neurons": "513", "activation": "RELU"},
                       {"number_of_neurons": "513", "activation": "RELU"}]
        }
        output_dict = createKerasModel(test_dict)
        model_test = json.loads(output_dict)
        for i in range(len(test_dict["layers"])):
            assert int(test_dict["layers"][i]["number_of_neurons"]) == model_test["config"]["layers"][i]["config"]["units"]
            assert test_dict["layers"][i]["activation"].lower() == model_test["config"]["layers"][i]["config"]["activation"]

    def test_two(self):

        test_dict = {
            "number_of_layers": "4",
            "optimizer": "Adam",
            "loss_function": "Binary CrossEntropy",
            "layers": [{"number_of_neurons": "613", "activation": "RELU"},
                       {"number_of_neurons": "613", "activation": "RELU"},
                       {"number_of_neurons": "613", "activation": "RELU"}]
        }
        output_dict = createKerasModel(test_dict)
        model_test = json.loads(output_dict)
        for i in range(len(test_dict["layers"])):
            assert int(test_dict["layers"][i]["number_of_neurons"]) == model_test["config"]["layers"][i]["config"]["units"]
            assert test_dict["layers"][i]["activation"].lower() == model_test["config"]["layers"][i]["config"]["activation"]

    def test_three(self):

        test_dict = {
            "number_of_layers": "5",
            "optimizer": "Adam",
            "loss_function": "Binary CrossEntropy",
            "layers": [{"number_of_neurons": "713", "activation": "RELU"},
                       {"number_of_neurons": "713", "activation": "RELU"},
                       {"number_of_neurons": "713", "activation": "RELU"}]
        }
        output_dict = createKerasModel(test_dict)
        model_test = json.loads(output_dict)
        for i in range(len(test_dict["layers"])):
            assert int(test_dict["layers"][i]["number_of_neurons"]) == model_test["config"]["layers"][i]["config"]["units"]
            assert test_dict["layers"][i]["activation"].lower() == model_test["config"]["layers"][i]["config"]["activation"]

    def test_four(self):
        model = tensorflow.keras.models.load_model("test/model.h5")
        (arch, weight) = kerasToIr(model)
        # output_arch = json.loads(arch)
        with open('weight.json', 'w') as fp:
            json.dump(weight, fp)
        with open('architecture.json') as f:
            input_arch = json.load(f)
        assert arch == input_arch
