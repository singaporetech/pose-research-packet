# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 14:03:58 2023

@author: FMLM
"""
import math

import numpy as np
import cv2

def get_Angles_3d(vector1,vector2):
    if vector2 is not None:
        dot_vec = np.dot(vector1, vector2)
        # Calculate the magnitudes of the vector and axis
        magnitude_vector1 = np.linalg.norm(vector1)
        magnitude_vector2 = np.linalg.norm(vector2)
        angle_vec = round(math.degrees(np.arccos(dot_vec / (magnitude_vector1 * magnitude_vector2))),0)
        return angle_vec
    else:    
        
        # Define the x, y, z unit vectors
        x_axis = np.array([1, 0, 0])
        y_axis = np.array([0, 1, 0])
        z_axis = np.array([0, 0, 1])
        
        # Calculate the dot product of the vector with each axis
        dot_x = np.dot(vector1, x_axis)
        dot_y = np.dot(vector1, y_axis)
        dot_z = np.dot(vector1, z_axis)
        
        # Calculate the magnitudes of the vector and axis
        magnitude_vector = np.linalg.norm(vector1)
        magnitude_x = np.linalg.norm(x_axis)
        magnitude_y = np.linalg.norm(y_axis)
        magnitude_z = np.linalg.norm(z_axis)
        
        # Calculate the angles
        angle_x = round(math.degrees(np.arccos(dot_x / (magnitude_vector * magnitude_x))),0)
        angle_y = round(math.degrees(np.arccos(dot_y / (magnitude_vector * magnitude_y))),0)
        angle_z = round(math.degrees(np.arccos(dot_z / (magnitude_vector * magnitude_z))),0)

        return angle_x, angle_y, angle_z
    
def display_ArmAngles(img,angle1,angle2,angle3,angle4):
    
    img = cv2.flip(img, 1)
    
    cv2.putText(img,"Shoulder rotation:"+str(angle1),(50,30), cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, (0,0, 255), 2, cv2.LINE_AA)
    cv2.putText(img,"Elbow rotation:"+" "+" Y:"+str(angle2),(50,50), cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, (0,0, 255), 2, cv2.LINE_AA)
    cv2.putText(img,"Wrist rotation:"+" "+" Y:"+str(angle3),(50,70), cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, (0,0, 255), 2, cv2.LINE_AA) 
    cv2.putText(img,"palm rotation:"+" "+" Y:"+str(angle4),(50,90), cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, (0,0, 255), 2, cv2.LINE_AA)
    
    cv2.imshow('Display',img)
    
    return None
    
    
    
    
    
    
    
    
    
    
    
    
    
    