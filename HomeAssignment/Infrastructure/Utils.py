import numpy as np
import cv2


class Utils:
    @staticmethod
    def rgb_to_hsv(rgb_image: np.ndarray) -> np.ndarray:
        """
        Convert an RGB image to HSV color space.
        :param rgb_image: The RGB image as a NumPy array.
        :return: The HSV image as a NumPy array.
        """
        return cv2.cvtColor(rgb_image.astype(np.uint8), cv2.COLOR_RGB2HSV).astype(np.float64) / 255.0

    @staticmethod
    def hsv_to_rgb(hsv_image):
        """
        Convert an HSV image to RGB color space.
        :param hsv_image: The HSV image as a NumPy array.
        :return: The RGB image as a NumPy array.
        """
        return cv2.cvtColor((hsv_image * 255).astype(np.uint8), cv2.COLOR_HSV2RGB).astype(np.float64)
