# pose-research-packet a.k.a Motion Retargetting Project

This project aims to explore how motion retargetting can be employed to immersify real-world tasks.

## Retargetting Architecture

This is the broad architecture of the current retargetting use case for drawing.

![immersification](https://github.com/singaporetech/pose-research-packet/assets/23288373/23e51b73-26d8-4204-8ccf-1b8798ca1d24)

### Human-Computer Retargetting

https://github.com/singaporetech/pose-research-packet/assets/23288373/6d2731a6-cbee-4eda-bc98-727ff686a4f1

### Human-Robot Retargetting

https://github.com/singaporetech/pose-research-packet/assets/23288373/24bd005b-b7f5-4666-a20e-c2a211595442

# Usable Artifact - 

The current library allows developers to perform various pose estimation in python and output pose angles in C# for motion retargeting of digital avatar for Unity3D. You can have a look at the demo video in this repo for an idea.

This repo uses various cameras thorugh the ChooseCam.py module to track user's facial or body markers to perform pose estimation. The tracking model can be call from the infer.py module. This can have many advantages over the use of traditional cumbersome wearerable sensors, including, cost, space constraint, ease of uses, among others; in many areas of research. 

## Setting up
For Python:
ver 3.8 or below (you can create a virtual environment for this and add it to your anaconda environment, I use python 3.8.12) The following version of the libraries need to be installed (remember to install it under the virtual environment)

```
> create environment conda create --name myenv python=3.8.12 conda activate myenv

> install TensorFlow conda install tensorflow=2.3.0

> install opencv conda install opencv=4.0.1

> install mediapipe pip install mediapipe==0.8.9.1

> install spyder pip install spyder
```

Add the virtual environment to youe anaconda environment list after installing all the above library

`conda config --add envs_dirs C:\Users\your_username\anaconda3\envs`

Subsequently to use spyder in the next session, just activate the environment.

`conda activate myenv`

In the activated environment, launch spyder.

You can also create a separate environment for python 3.9 and above, however you will also need to have the corresponding versions of the python libraries for python 3.9 or higher.

# Related publication 

The following bibtex can be used to cite our pilot study on a head tracking exergame presented in the AAAI Summer Symposium 2023.

```
@inproceedings{quah2023trackingexergame,
    title={A Portable Vision-Based Head Tracking Exergame Solution for Neck Rehabilitation},
    author={Chee Kwang Quah, Jinhhao Ng, Benjamin Soon},
    booktitle={Proceedings of the AAAI Symposium Series},
    volume={1},
    number={1},
    pages={23--27},
    issue_date = {November 2023},
    publisher = {AAAI Press},
    address = {Washington, DC, USA}
}
```

For enquiries, please contact: cheekwang.quah, jinhhao.ng, benjamin.soon@singaporetech.edu.sg






