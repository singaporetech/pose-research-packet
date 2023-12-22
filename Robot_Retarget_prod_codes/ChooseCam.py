# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:26:44 2023

@author: FMLM
"""
import cv2
import pyrealsense2 as rs
import numpy as np
  
class Camera:
    def __init__(self):
        self.is_initialized = False

    def initialize(self):
        raise NotImplementedError("Subclasses must implement the initialize method.")

    def get_frames(self):
        raise NotImplementedError("Subclasses must implement the get_frames method.")

class Webcam(Camera):
    def initialize(self):
        self.cap = cv2.VideoCapture(0)

    def get_frames(self):
        ret, frame = self.cap.read()
        return frame

class DepthCamera(Camera):
    def initialize(self):
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.align = rs.align(rs.stream.color)

        # Enable depth and color streams
        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)

        # Start the pipeline
        self.profile = self.pipeline.start(self.config)

    def get_frames(self):
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        # Align the depth and color frames for D435i
        if depth_frame is not None and color_frame is not None:
            aligned_frames = self.align.process(frames)
            color_frame = aligned_frames.get_color_frame()
            depth_frame = aligned_frames.get_depth_frame()
            self.depth_intrinsics = self.profile.get_stream(rs.stream.depth).as_video_stream_profile().get_intrinsics()
            ret=1
        else:
            color_frame = frames.get_color_frame()
            depth_frame = frames.get_depth_frame()
            ret=1

        # Convert frames to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())
        color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)
        depth_image = np.asanyarray(depth_frame.get_data())

        return ret,color_image, depth_image
    
    def CAM_3Dcoord(self,raw_coord):
        coord_3d = []
        
        for i in range(len(raw_coord)):
            coord_3d.append(rs.rs2_deproject_pixel_to_point(self.depth_intrinsics, [raw_coord[i][0], raw_coord[i][1]], raw_coord[i][2]))
        
        return coord_3d
      
