"""
    OpenCV wrapper.
"""

import cv2 as cv


def read_img(img_name):
    return cv.imread(img_name)

def resize(img, height, width):
    return cv.resize(img, (width, height), interpolation=cv.INTER_AREA)

def enable_webcam():
    return cv.VideoCapture(0)

def convert_to_HSV(frame):
    return cv.cvtColor(frame, cv.COLOR_BGR2HSV)

def create_mask(hsv, lower_bound, upper_bound):
    return cv.inRange(hsv, lower_bound, upper_bound)

def inverse_mask(mask):
    return cv.bitwise_not(mask)

def apply_mask(frame, mask):
    return cv.bitwise_and(frame, frame, mask=mask)

def show_frame(name, frame):
    cv.imshow(name, frame)

def esc_pressed():
    return cv.waitKey(1) == 27

def clean_up(vid):
    vid.release()
    cv.destroyAllWindows()
