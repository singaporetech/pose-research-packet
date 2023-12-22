# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 14:24:42 2023

@author: FMLM
"""

import mediapipe as mp

class poses:
    def __init__(self):
        self.is_initialized = False

    def initialize(self):
        raise NotImplementedError("Subclasses must implement the initialize method.")

    def get_joints(self):
        raise NotImplementedError("Subclasses must implement the get_joints method.")
        
    def extract_joints(self):
        raise NotImplementedError("Subclasses must implement the extract_joints method.")
        
class MPBody(poses):
  
    def initialize(self):
        
        #initialize mediapipe pose
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=0.3,
            min_tracking_confidence=0.3)

    def get_joints(self,image):
        image.flags.writeable = False
        self.img = image
        self.results_pose = self.pose.process(self.img)
        
        return self.results_pose
    
    def extract_joints(self,joints_body,depth_image):
        coord_3d = []
        if self.results_pose.pose_landmarks:
            for idx, lmk in enumerate(self.results_pose.pose_landmarks.landmark):
                if idx in joints_body and lmk.visibility >0.5:
                    if 0<int(lmk.x * self.img.shape[1])<640 and 0<int(lmk.y * self.img.shape[0])<480:
                        z = depth_image[int(lmk.y * self.img.shape[0]), int(lmk.x * self.img.shape[1])]
                        coord_3d.append([int(lmk.x * self.img.shape[1]), int(lmk.y * self.img.shape[0]),z])
                        #image = cv2.circle(self.img, (int(lmk.x * image.shape[1]), int(lmk.y * image.shape[0])), 5, (0, 255, 0), -1)
        
        return coord_3d
        
class MPHand(poses):
        
    def initialize(self):

        self.mp_hands = mp.solutions.hands    #for retargeting of gripping motion in future
        self.hands = self.mp_hands.Hands(
            model_complexity=0,
            # NEW
            max_num_hands=1,
            min_detection_confidence=0.3,
            min_tracking_confidence=0.3)
        
    def get_joints(self,image):
        image.flags.writeable = False
        self.img = image
        self.hand_pose = self.hands.process(self.img)
        
        return self.hand_pose
    
    def extract_joints_3D(self,joints_hand,depth_image):
        coord_3d = []
        if self.hand_pose.multi_hand_landmarks:
            for hand_landmarks in self.hand_pose.multi_hand_landmarks:
                for idx, lmk in enumerate(hand_landmarks.landmark):
                    if idx in joints_hand:
                        #if all 3 keypoints are within the image
                        if 0<int(lmk.x * self.img.shape[1])<640 and 0<int(lmk.y * self.img.shape[0])<480:
                            z = depth_image[int(lmk.y * self.img.shape[0]), int(lmk.x * self.img.shape[1])]
                            coord_3d.append([int(lmk.x * self.img.shape[1]), int(lmk.y * self.img.shape[0]), z])
        
        return coord_3d

    def extract_joints_2D(self,joints_hand):
        coord_2d = []
        if self.hand_pose.multi_hand_landmarks:
            for hand_landmarks in self.hand_pose.multi_hand_landmarks:
                for idx, lmk in enumerate(hand_landmarks.landmark):
                    if idx in joints_hand:
                        #if all 3 keypoints are within the image
                        if 0<int(lmk.x * self.img.shape[1])<640 and 0<int(lmk.y * self.img.shape[0])<480:
                            coord_2d.append([int(lmk.x * self.img.shape[1]), int(lmk.y * self.img.shape[0])])
        
        return coord_2d
    
            
