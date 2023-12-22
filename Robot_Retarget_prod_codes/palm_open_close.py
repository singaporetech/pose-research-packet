import cv2
import numpy as np
# NEW
import serial
import time

from ChooseCam import Webcam
from Infer import MPHand

# indices for the hand joints that you want to extract
# joints_hand = [8, 12, 16, 20]
joints_hand = [0, 9, 12, 13, 16]

Camera = Webcam()
Camera.initialize()

handJoints = MPHand()
handJoints.initialize()

prev_status = "0"

# NEW

# Algorithm For Closed Hand Detection
def open_close_hand(coord):
    if coord == 0:
        pass
    else:
        # Note: Do NOT use absolute value
        palm = coord[0]
        middle_joint = coord[1]
        middle_tip = coord[2]     
        ring_joint = coord[3]
        ring_tip = coord[4]

        # Using Euclidean distance formula, which is the square root of the sum of the squares of the differences in x and y
        # coordinates between two points
        middle_tip_palm_dist = ((middle_tip[0] - palm[0]) ** 2 + (middle_tip[1] - palm[1]) ** 2) ** 0.5
        middle_joint_palm_dist = ((middle_joint[0] - palm[0]) ** 2 + (middle_joint[1] - palm[1]) ** 2) ** 0.5

        ring_tip_palm_dist = ((ring_tip[0] - palm[0]) ** 2 + (ring_tip[1] - palm[1]) ** 2) ** 0.5
        ring_joint_palm_dist = ((ring_joint[0] - palm[0]) ** 2 + (ring_joint[1] - palm[1]) ** 2) ** 0.5

    if middle_joint_palm_dist > middle_tip_palm_dist and ring_joint_palm_dist > ring_tip_palm_dist:
        # Closed Hand
        return 1
    else:
        # Open Hand
        return 0

# "int main"
if __name__ == "__main__":

    while True:
        color_frame= Camera.get_frames()
        color_image = color_frame.copy()

        handJoints.get_joints(color_image)
        coord2D_hand = handJoints.extract_joints_2D(joints_hand)

        if len(coord2D_hand) >= 5:
            # NEW
            # Set "display_text" as blank first
            display_text = ""

            # Call open hand function
            open_close_hand(coord2D_hand)
            
            # Display "Closed" or "Open" Text on screen
            if open_close_hand(coord2D_hand) == 0:
                display_text = "Open"
                cur_status = "0"

            elif open_close_hand(coord2D_hand) == 1:
                display_text = "Closed"
                cur_status = "1"

            if cur_status == prev_status:
                pass
    
            for i in range(len(coord2D_hand)):
                color_image = cv2.circle(color_image, (coord2D_hand[i][0], coord2D_hand[i][1]), 5, (0, 255, 0), -1)

            # Put text on the live feed
            color_image = cv2.flip(color_image, 1)

            # NEW
            # Display Text
            text = display_text
            position = (50, 50)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            text_color = (0, 255, 0)  # Green color in BGR format
            thickness = 2
            line_type = cv2.LINE_AA
            cv2.putText(color_image, text, position, font, font_scale, text_color, thickness, line_type)

            cv2.imshow('Display', color_image)

        else:
            color_image = cv2.flip(color_image, 1)
            cv2.imshow('Display', color_image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
