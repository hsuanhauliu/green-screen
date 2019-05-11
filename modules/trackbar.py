"""
    OpenCV track bar to control HSV upper bound and lower bound.
"""

import cv2 as cv
import numpy as np


# Constants
MIN_HSV = [0, 0, 0]
MAX_HSV = [179, 255, 255]

class HSVTrackbar():
    """ HSV tracker class """

    def __init__(self, name="Control Panel", height=1, width=700):
        self.trackbar_name = name
        self.trackbar_size = np.zeros([height, width], np.uint8)
        cv.namedWindow(self.trackbar_name)

        self.lower_bound = np.array(MIN_HSV)
        self.upper_bound = np.array(MAX_HSV)

        # create sliders
        cv.createTrackbar("L - h", self.trackbar_name, 0, 179, self.set_l_h)
        cv.createTrackbar("U - h", self.trackbar_name, 179, 179, self.set_u_h)
        cv.createTrackbar("L - s", self.trackbar_name, 0, 255, self.set_l_s)
        cv.createTrackbar("U - s", self.trackbar_name, 255, 255, self.set_u_s)
        cv.createTrackbar("L - v", self.trackbar_name, 0, 255, self.set_l_v)
        cv.createTrackbar("U - v", self.trackbar_name, 255, 255, self.set_u_v)

    def set_l_h(self, val):
        self.lower_bound[0] = val

    def set_l_s(self, val):
        self.lower_bound[1] = val

    def set_l_v(self, val):
        self.lower_bound[2] = val

    def set_u_h(self, val):
        self.upper_bound[0] = val

    def set_u_s(self, val):
        self.upper_bound[1] = val

    def set_u_v(self, val):
        self.upper_bound[2] = val

    def show_trackbar(self):
        cv.imshow(self.trackbar_name, self.trackbar_size)
