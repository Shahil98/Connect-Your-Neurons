from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """
    Returns index.html when a request is made to "/".
    """
    return render_template('index.html', title='Connect Your Neurons')


@app.route('/get_keras_model', methods=['POST'])
def get_keras_model():
    """
    Returns a keras model to the
    user when a request is made to "/get_keras_model"
    """
    json_file = request.form["architecture_parameters"]
    print(eval(json_file))
    return ("Work in progress")
