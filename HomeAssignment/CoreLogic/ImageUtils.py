import numpy as np
import cv2


class ImageUtils:
    @staticmethod
    def rgb_to_hsv(rgb_image: np.ndarray) -> np.ndarray:
        """
        Convert an RGB image to HSV color space.
        :param rgb_image: The RGB image as a NumPy array.
        :return: The HSV image as a NumPy array.

        Note: This function and the following one was suggested after looking out for
        how to transform from RGB to HSV vice versa.
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

    @staticmethod
    def multi_channel_filter_apply(image: np.ndarray, filter_func) -> np.ndarray:
        """
        Apply a filter to multiple channels of an image.
        :param image: The image as a NumPy array.
        :param filter_func: The filter function to apply.
        :return: The modified image with the filter applied.
        """
        # Split the image into its RGB channels
        red_channel = image[:, :, 0]
        green_channel = image[:, :, 1]
        blue_channel = image[:, :, 2]

        # Apply the filter to each channel
        red_result = filter_func(red_channel)
        green_result = filter_func(green_channel)
        blue_result = filter_func(blue_channel)

        # Combine the results back into a single image
        result = np.zeros_like(image)
        result[:, :, 0] = red_result
        result[:, :, 1] = green_result
        result[:, :, 2] = blue_result

        return result.astype(np.uint8)

    @staticmethod
    def convert_to_3d(image: np.ndarray) -> np.ndarray:
        """
        Convert a 2D grayscale image to a 3D grayscale image.
        :param image: The 2D grayscale image as a NumPy array.
        :return: The 3D grayscale image as a NumPy array.
        """
        if len(image.shape) == 2:
            return np.stack((image,) * 3, axis=-1)
        return image


