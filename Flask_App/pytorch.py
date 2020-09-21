import torch
import json
f = open('data.json',)
architecture_parameters = json.load(f)
optimizer = architecture_parameters["optimizer"]
loss_function = architecture_parameters["loss_function"]
layers = architecture_parameters["layers"]
former_layer = layers[0]
print(former_layer["number_of_neurons"])
pytorch_layers = []
for layer in layers[1:]:
    pytorch_layers.append(torch.nn.Linear(int(former_layer["number_of_neurons"]), int(layer["number_of_neurons"])))
    if(layer["activation"] == "RELU"):
        torch.nn.ReLU()
    elif(layer["activation"] == "TANH"):
        torch.nn.Tanh()
    else:
        torch.nn.Sigmoid()
    former_layer["number_of_neurons"] = layer["number_of_neurons"]
print(pytorch_layers)   
model = torch.nn.Sequential(*pytorch_layers)
print(model)
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
print(model)
torch.save(model.state_dict(), 'model.pth')
