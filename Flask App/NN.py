from keras.models import Sequential
from keras.layers import Dense
import keras
import pandas as pd
from sklearn.model_selection import train_test_split
import json
# load json input from json file
f = open('data.json',)
json_data = json.load(f)
num_layer = json_data["number_of_layers"]
num_hidden_layer = len(json_data["layers"])
activation_function_list = []
num_cell_list = []
for item in json_data["layers"]:
    num_cell_list.append(item["number_of_neurons"])
    activation_function_list.append(item["activation"].lower())
print(num_cell_list)
print(activation_function_list)
opt = json_data["optimizer"]
loss_function = json_data["loss_function"]
# data pre-processing
dataset = pd.read_csv('haberman.csv')
X = dataset.iloc[:, 0:3]
y = dataset.iloc[:, 3]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
input_size = 3
epoch = 20
batch_size = 5
# NN function
def NN(X, y, opt, num_hidden_layer, activation_function_list, num_cell_list, input_size, epoch=100, batch_size=5):
    model = Sequential()
    model.add(Dense(12, input_dim=input_size, activation='relu'))
    for i in range(num_hidden_layer):
        model.add(Dense(num_cell_list[i], activation=activation_function_list[i]))
    model.add(Dense(1, activation='sigmoid'))
    #opt = keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(loss="binary_crossentropy",optimizer=opt, metrics=['accuracy'])
    model.fit(X, y, epochs=epoch, batch_size=batch_size)
    _, accuracy = model.evaluate(X, y)
    print("Accuracy: %.2f" % (accuracy*100))


NN(X_train, y_train, opt, num_hidden_layer, activation_function_list, num_cell_list, input_size, epoch, batch_size)
