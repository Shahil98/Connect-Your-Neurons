from keras.models import Sequential
from keras.layers import Dense
import keras
import pandas as pd
from keras.utils.vis_utils import plot_model
from sklearn.model_selection import train_test_split
import json
# load json input from json file
f = open('data.json',)
data = json.load(f)
learning_rate, num_hidden_layer, activation_function,input_size,epoch,batch_size = data['user_input']
# data pre-processing
dataset = pd.read_csv('haberman.csv')
X = dataset.iloc[:,0:3]
y = dataset.iloc[:,3]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.25,random_state = 0)

# NN function
def NN(X,y,learning_rate,num_hidden_layer,activation_function,input_size,epoch=100,batch_size=5):
  model = Sequential()
  model.add(Dense(12, input_dim=input_size,activation='relu'))
  for i in range(num_hidden_layer):
    model.add(Dense(6,activation=activation_function))
  model.add(Dense(1,activation='sigmoid'))
  opt = keras.optimizers.Adam(learning_rate=learning_rate)
  model.compile(loss="binary_crossentropy",optimizer=opt,metrics=['accuracy'])
  model.fit(X,y,epochs=epoch,batch_size=batch_size)
  #plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
  _,accuracy = model.evaluate(X,y)
  print("Accuracy: %.2f" %(accuracy*100))
NN(X_train,y_train,learning_rate, num_hidden_layer, activation_function,input_size,epoch,batch_size)
