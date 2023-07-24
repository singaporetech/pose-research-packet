# Motion Retargeting 

Perform various pose estimation in python and output pose angles in C# for motion retargeting of digital avatar for Unity3D. You can have a look at the demo video in this repo for an idea.

# Background
This repo uses various cameras thorugh the ChooseCam.py module to track user's facial or body markers to perform pose estimation. The tracking model can be call from the infer.py module. This can have many advantages over the use of traditional cumbersome wearerable sensors, including, cost, space constraint, ease of uses, among others; in many areas of research. 

Setting up
For Python:

ver 3.8 or below (you can create a virtual environment for this and add it to your anaconda environment, I use python 3.8.12) The following version of the libraries need to be installed (remember to install it under the virtual environment)

#create environment conda create --name myenv python=3.8.12 conda activate myenv

#install TensorFlow conda install tensorflow=2.3.0

#install opencv conda install opencv=4.0.1

#install mediapipe pip install mediapipe==0.8.9.1

#install spyder pip install spyder

#add the virtual environment to youe anaconda environment list after installing all the above library conda config --add envs_dirs C:\Users\your_username\anaconda3\envs

#subsequently to use spyder in the next session, just activate the environment conda activate myenv #in the activated environment, launch spyder spyder

You can also create a seperate environment for python 3.9 and above, however you will also need to have the corresponding versions of the python libraries for python 3.9 or higher
