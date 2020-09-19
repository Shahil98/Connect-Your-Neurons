
import sys
sys.path.insert(0, "../")
from code.main import create_keras_model


def test_one():

    test_dict = {
        "number_of_layers": "3",
        "optimizer": "Adam",
        "loss_function": "Binary CrossEntropy",
        "layers": [{"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}, {"number_of_neurons": "513", "activation": "RELU"}]
    }
    model_test = create_keras_model(test_dict)
    assert model_test == test_dict


test_one()
