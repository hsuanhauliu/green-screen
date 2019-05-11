"""
    A program that allows you to create your own green screen effect.
"""

from modules.cv_wrapper import *
from modules.trackbar import HSVTrackbar
from modules.util import *


def main():
    """ Start of the program """
    args = parse_inputs()
    background = read_img(args.bg_name)
    height, width = calculate_size(background.shape[0],
                                   background.shape[1],
                                   args.resize)
    resized_bg = resize(background, height, width)
    webcam = enable_webcam()
    trackbar = HSVTrackbar()

    while True:
        _, frame = webcam.read()
        frame = resize(frame, height, width)
        hsv = convert_to_HSV(frame)

        mask = create_mask(hsv, trackbar.lower_bound, trackbar.upper_bound)
        mask_inv = inverse_mask(mask)

        foreground = apply_mask(frame, mask_inv)
        new_frame = resized_bg.copy()

        mix_foreground(foreground, new_frame, mask_inv)

        show_frame("Result", new_frame)
        trackbar.show_trackbar()

        if esc_pressed():
            break

    clean_up(webcam)


if __name__ == "__main__":
    main()
