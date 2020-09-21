from flask import Flask, render_template, request, send_file
app = Flask(__name__)


@app.route('/')
def index():
    """
    Function to render index.html when a request is made to "/".
    """

    return render_template('index.html', title='Connect Your Neurons')


@app.route('/get_keras_model', methods=['POST'])
def getKerasModel():
    """
    Function to send a keras model architecture to the
    user when a request is made to "/get_keras_model"
    """

    json_file = request.form["keras_architecture_parameters"]
    model_json = createKerasModel(eval(json_file))

    with open("static/model.json", "w") as json_file:
        json_file.write(model_json)

    return send_file("static/model.json", attachment_filename="model.json",
                     as_attachment=True)


@app.route('/get_pytorch_model', methods=['POST'])
def getPytorchModel():
    """
    Function to send a pytorch model to the
    user when a request is made to "/get_pytorch_model"
    """

    return("Work In Progress")


def createKerasModel(architecture_parameters):
    """
    Function to create a keras architecture file based on input parameters.

    Parameters
    ----------
    architecture_parameters: dictionary
        Dictionary describing model architecture parameters

    Returns
    -------
    model_json
        json file describing model architecture that can be used by keras
    """

    import tensorflow as tf

    optimizer = architecture_parameters["optimizer"] 
    loss_function = architecture_parameters["loss_function"]
    layers = architecture_parameters["layers"]

    model = tf.keras.Sequential()

    for layer in layers:

        if(layer["activation"] == "RELU"):
            layer["activation"] = "relu"
        elif(layer["activation"] == "TANH"):
            layer["activation"] = "tanh"
        elif(layer["activation"] == "SOFTMAX"):
            layer["activation"] = "softmax"
        else:
            layer["activation"] = "sigmoid"

        model.add(tf.keras.layers.Dense(int(layer["number_of_neurons"]),
                                        activation=layer["activation"]))

    if(loss_function == "BINARY CROSS ENTROPY"):
        loss_function = "binary_crossentropy"
    elif(loss_function == "CATEGORICAL CROSS ENTROPY"):
        loss_function = "categorical_crossentropy"
    elif(loss_function == "MEAN ABSOLUTE ERROR"):
        loss_function = "mean_absolute_error"
    else:
        loss_function = "mean_squared_error"

    if(optimizer == "ADAM"):
        optimizer = "adam"
    elif(optimizer == "SGD"):
        optimizer = "sgd"
    elif(optimizer == "ADAGRAD"):
        optimizer = "adagrad"
    else:
        optimizer = "rmsprop"

    model.compile(loss=loss_function, optimizer=optimizer, 
                  metrics=["accuracy"])

    model_json = model.to_json()

    return(model_json)


def kerasToIr(model):
    """
    Function to convert from keras model to Intermediate Representation.

    Parameters
    ----------
    model: Sequential class object
        Obtained by loading keras model from HDF file

    Returns
    -------
    model_architecture
        A dictionary containing information about model architecture
    model_weights
        A dictionary containing bias and kernel weights
    """

    import tensorflow as tf

    optimizer_dictionary = {
        "RMSPROP": tf.keras.optimizers.RMSprop,
        "ADAM": tf.keras.optimizers.Adam,
        "SGD": tf.keras.optimizers.SGD,
        "ADAGRAD": tf.keras.optimizers.Adagrad
    }

    loss_function_dictionary = {
        "categorical_crossentropy": "CATEGORICAL CROSS ENTROPY",
        "binary_crossentropy": "BINARY CROSS ENTROPY",
        "mean_absolute_error": "MEAN ABSOLUTE ERROR",
        "mean_squared_error": "MEAN SQUARED ERROR"
    }

    activation_function_dictionary = {
        "relu": "RELU",
        "tanh": "TANH",
        "sigmoid": "SIGMOID",
        "softmax": "SOFTMAX"
    }

    model_architecture = {}

    optimizer = model.optimizer
    for key in optimizer_dictionary.keys():
        if(isinstance(model.optimizer, optimizer_dictionary[key])):
            optimizer = key

    model_architecture["optimizer"] = optimizer

    model_architecture["loss_function"] = loss_function_dictionary[model.loss]

    model_architecture["number_of_layers"] = str(len(model.layers))

    model_architecture["layers"] = []

    model_bias_values = {}
    model_kernel_values = {}

    layer_id = 1

    for layer in model.layers:
        layer_parameters = {}
        layer_name = "layer_" + str(layer_id)
        layer_config = layer.get_config()
        layer_parameters["number_of_neurons"] = str(layer_config["units"])
        layer_parameters["activation"] = activation_function_dictionary[layer_config["activation"]]
        layer_parameters["type"] = "DENSE"
        layer_parameters["name"] = layer_name
        model_architecture["layers"].append(layer_parameters)
        weights = layer.get_weights()
        model_kernel_values[layer_name] = weights[0]
        model_bias_values[layer_name] = weights[1]
        layer_id += 1

    model_weights = {
        "bias_weights": model_bias_values,
        "kernel_weights": model_kernel_values
    }
    return(model_architecture, model_weights)
