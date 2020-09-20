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
    json
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
        else:
            layer["activation"] = "sigmoid"

        model.add(tf.keras.layers.Dense(int(layer["number_of_neurons"]),
                                        activation=layer["activation"]))

    if(loss_function == "BINARY CROSSENTROPY"):
        loss_function = "binary_crossentropy"
    elif(loss_function == "CATEGORICAL CROSSENTROPY"):
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
