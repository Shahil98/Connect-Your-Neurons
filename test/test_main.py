
from main import create_keras_model


def test_one():

    input_dict = {
        "number_of_layers": "3",
        "optimizer": "Adam",
        "loss_function": "Binary CrossEntropy",
        "layers": [{"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}]
    }
    model_test = create_keras_model(input_dict)

    for i in range(len(input_dict["layers"])):
        assert int(input_dict["layers"][i]["number_of_neurons"]) == model_test["config"]["layers"][i]["config"]["units"]
        assert input_dict["layers"][i]["activation"].lower() == model_test["config"]["layers"][i]["config"]["activation"]


test_one()
