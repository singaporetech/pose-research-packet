import cv2
import numpy as np
import socket
from XOR_CheckSum import xor_checksum_string

import utils 

from ChooseCam import DepthCamera
from Infer import MPBody,MPHand

#indices of left and right shoulder, left elbow and left wrist
joints_body = [11, 12, 13, 15]
#indices for index finger tip
joints_hand = [8]

realSenseCamera = DepthCamera()
realSenseCamera.initialize()

bodyJoints = MPBody()
bodyJoints.initialize()

handJoints = MPHand()
handJoints.initialize()

# Set up the IP address and port number of the robot server
server_address = ('192.168.0.100', 5890)
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the server
client_socket.connect(server_address)

if __name__ == "__main__":
    
    while True:
        
        ret,color_frame, depth_image = realSenseCamera.get_frames()
        color_image = color_frame.copy()
        if ret!=1:
          continue
        
        bodyJoints.get_joints(color_image)
        handJoints.get_joints(color_image)
  
        coord3D_body = bodyJoints.extract_joints(joints_body,depth_image)
        coord3D_hand = handJoints.extract_joints(joints_hand,depth_image)
        coord_3d = coord3D_body + coord3D_hand
        
        if len(coord_3d) >= 5:
            for i in range(len(coord_3d)):
                color_image = cv2.circle(color_image, (coord_3d[i][0], coord_3d[i][1]), 5, (0, 255, 0), -1)
            
            coord_3d_Cam = realSenseCamera.CAM_3Dcoord(coord_3d)
            
            shoulder_joint = np.array(coord_3d_Cam[1])-np.array(coord_3d_Cam[0])
            elbow_joint = np.array(coord_3d_Cam[2]) -np.array(coord_3d_Cam[0])
            wrist_joint = np.array(coord_3d_Cam[3]) - np.array(coord_3d_Cam[2])
            palm_joint = np.array(coord_3d_Cam[4]) - np.array(coord_3d_Cam[3])
            
            Elbox_angleX, Elbox_angleY, Elbox_angleZ = utils.get_Angles_3d(elbow_joint,vector2=None)
            Elbox_angleY = 180-Elbox_angleY
            
            Wrist_angleX, Wrist_angleY, Wrist_angleZ  = utils.get_Angles_3d(wrist_joint,vector2=None) #wrist angle w.r.t elbow joint
            Wrist_angle = utils.get_Angles_3d(wrist_joint,elbow_joint) #wrist angle w.r.t elbow vector 
            Wrist_angle = -1*(Wrist_angle)+180
            
            Palm_angle = utils.get_Angles_3d(palm_joint,wrist_joint) #wrist angle w.r.t elbow vector (for robot only)
            
            shoulder_joint[1] = 0
            wrist_joint[1] = 0
            shoulder_angle = utils.get_Angles_3d(shoulder_joint,wrist_joint)
            
            utils.display_ArmAngles(color_image,shoulder_angle,Elbox_angleY,Wrist_angle,Palm_angle)
            
        else:    
            color_image = cv2.flip(color_image, 1)
            cv2.imshow('Display',color_image)
            
        if cv2.waitKey(5) & 0xFF == ord('q'):
          break
      
    cv2.destroyAllWindows()
        