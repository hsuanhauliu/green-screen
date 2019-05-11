"""
    Utility file that contains helper functions.
"""

import argparse
import numpy as np


def parse_inputs():
    """ Parse inputs from terminal """
    parser = argparse.ArgumentParser()
    parser.add_argument("bg_name", type=str,
                        help="Choose a background picture that you like")
    parser.add_argument("-r", "--resize", type=int, default=100,
                        help="Input a percentage to resize window")
    return parser.parse_args()

def calculate_size(height, width, percentage):
    """ Calculate resized height and width """
    new_height = int(height * (percentage / 100))
    new_width = int(width * (percentage / 100))
    return new_height, new_width

def mix_foreground(foreground, frame, mask):
    """ Blend foreground into background """
    for (i, j), val in np.ndenumerate(mask):
        if val:
            frame[i, j] = foreground[i, j]
