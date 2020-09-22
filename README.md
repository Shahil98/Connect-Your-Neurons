<p align="center">
  <img
    width="200"
    src="https://raw.githubusercontent.com/Zhuolin0212/Connect-Your-Neurons/master/logo.png"
    alt="Connect-Your-Neurons"
  />
</p>
<p align="center">
  <a href="https://img.shields.io/github/commit-activity/m/Zhuolin0212/Connect-Your-Neurons?style=plastic"
    ><img
      src="https://img.shields.io/github/commit-activity/m/Zhuolin0212/Connect-Your-Neurons?style=plastic"
      alt="GitHub commit activity"
  /></a>
  <a href="https://github.com/Zhuolin0212/Connect-Your-Neurons/blob/master/LICENSE"
    ><img
      src="https://img.shields.io/github/license/Zhuolin0212/Project1?style=plastic"
      alt="GitHub"
  /></a>
  <a href="https://img.shields.io/badge/version-0.01-brightgreen"
    ><img
      src="https://img.shields.io/badge/version-0.01-brightgreen"
      alt="Version"/></a
  ><br />
  <a href="https://travis-ci.org/Zhuolin0212/Connect-Your-Neurons.svg?branch=master)](https://travis-ci.org/Zhuolin0212/Connect-Your-Neurons"
    ><img
      src="https://travis-ci.org/Zhuolin0212/Connect-Your-Neurons.svg?branch=master"
      alt="Build Status"
  /></a>
 <a href="https://doi.org/10.5281/zenodo.4023294"
    ><img 
      src="https://zenodo.org/badge/DOI/10.5281/zenodo.4023294.svg" 
      alt="DOI"
 ></a>
 <a href="https://codecov.io/gh/Zhuolin0212/Connect-Your-Neurons"
    ><img src="https://codecov.io/gh/Zhuolin0212/Connect-Your-Neurons/branch/master/graph/badge.svg" 
 /></a>
</p>


<!-- This is commented out. 

<<<<<<< HEAD
<<<<<<< HEAD
# Connect Your Neurons
=======
>>>>>>> 4875d19dd8a0f9b6c98e38da57ecb78e02f12ba1

=======
# Connect Your Neurons
[comment]: <> (![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Zhuolin0212/Connect-Your-Neurons?style=plastic))
[comment]: <> (![GitHub](https://img.shields.io/github/license/Zhuolin0212/Project1?style=plastic))
[comment]: <> (![Version](https://img.shields.io/badge/version-0.01-brightgreen))
[comment]: <> ([![Build Status](https://travis-ci.org/Zhuolin0212/Connect-Your-Neurons.svg?branch=master)](https://travis-ci.org/Zhuolin0212/Connect-Your-Neurons))
[comment]: <> ([![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4023294.svg)](https://doi.org/10.5281/zenodo.4023294))
=======
>>>>>>> 4875d19dd8a0f9b6c98e38da57ecb78e02f12ba1

>>>>>>> 75344f79e9df9c679f180ff7905048137f982ea0  
-->
>**Quick:** Quick prototyping :rocket:  
>**Convenience:** Convert trained models between different frameworks on the go :recycle:  
>**Support:** Works for every major deep learning framework :100:  
>**Easy:** Interactive GUI :computer:  

# ▶</strong> Youtube Link
[![Youtube](http://img.youtube.com/vi/H0h6bSO6XEI/0.jpg)](http://www.youtube.com/watch?v=H0h6bSO6XEI "111")

# 💡 Installation & Getting Started
1) Clone this repository
```
git clone https://github.com/Zhuolin0212/Connect-Your-Neurons.git
```
2) Execute ```pip install -r requirements.txt``` to install all necessary libraries.
3) Open Flask_App folder and execute ```set FLASK_APP=main.py``` command in cmd if you are using windows or in bash shell if you are using either Linux or Mac.
4) Execute ```flask run``` command in cmd if you are using windows or in bash shell if you are using either Linux or Mac to start the application at ```http://localhost:5000```.

# ❓ What is Connect Your Neurons?
1) Connect Your Neurons can help users rapidly prototype neural networks with GUI. When starting a deep learning project often we initially want to quickly build protoypes to get initial results. We plan to deliver a web application where users can quickly select a network architecture using a GUI and get the architecture file of the network in one of the major deep learning framework's of user's choice.
2) It can help users convert trained models between frameworks easily and efficiently. Many times a deep learning project's requirements changes and we want to have the same trained model but in a different framework. We plan to deliver a conversion tool for trained models between major deep learning frameworks. Our approach is to first convert a trained model into an intermediate representation and then convert to the deep learning framework of user's choice. The intermediate representation are two dictionaries, one for weights and one for architecture and has the following structure:

Model Architecture Dictionary For Intermediate Representation 
```
{
  "optimizer": optimizer name,
  "loss_function": loss function name,
  "number_of_layers": number of layers,
  "layers": [
              {"name": "layer_1", "activation": activation name, 
               "number_of_neurons": number of neurons, "type": layer type},
               ....
            ]
}
```

Model Weights Dictionary For Intermediate Representation
```
{
  "bias_weights": [
                   "layer_1": [ bias values for layer_1 ],
                   ...
                  ],
  "kernel_weights": [
                    "layer_1": [ kernel_weights for layer_1 ].
                    ...
                   ]
}
```

# 🙋 Why Jump To This Project
If you jump to our group project, you will be contributing to a cool project and learn along the way. We have already added features like gui to select network architecture, functionality to convert from a trained keras model to an intermediate representation, functionality to generate a keras architecture from the network parameters provided and you just need to keep the momentum going. We know that some of you may not have the necessary knowledge to build this software, but we can assure you that you just require some basic fundamental skills like python and machine learning to work on this project and build the software. 

# 📝 License
Copyright © 2020-present, [Contributors](https://github.com/Zhuolin0212/Connect-Your-Neurons/graphs/contributors).<br>
This project is [MIT](https://github.com/Zhuolin0212/Connect-Your-Neurons/blob/master/LICENSE) licensed.

# :ballot_box_with_check: Self-Assessment 
[Check assessment](https://github.com/Zhuolin0212/Connect-Your-Neurons/blob/master/PROJ1-selfAssessment.md)
