from CoreLogic.Operations.BaseOperation import BaseOperation
import numpy as np


class EdgeDetection(BaseOperation):
    def __init__(self):
        self.sobel_x = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])

        self.sobel_y = np.array([
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ])

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the edge detection operation on a color image.
        The image is split into its RGB channels, and the Sobel operator is applied to each channel.
        The results are combined to form the final image.
        :param image: The image as a NumPy array.
        :return: The modified image with edges detected.
        """
        red_channel = image[:, :, 0]
        green_channel = image[:, :, 1]
        blue_channel = image[:, :, 2]

        red_result = self.padded_conv(red_channel)
        green_result = self.padded_conv(green_channel)
        blue_result = self.padded_conv(blue_channel)

        result = np.zeros_like(image)
        result[:, :, 0] = red_result
        result[:, :, 1] = green_result
        result[:, :, 2] = blue_result

        return result.astype(np.uint8)

    def padded_conv(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the Sobel operator to the image using a padded convolution.
        The Sobel operator is used to detect edges in the image.
        The image is padded to handle the borders.
        :param image: The image as a NumPy array.
        :return: The modified image with edges detected.
        """
        image = image.astype(np.float32)
        padded = np.pad(image, ((1, 1), (1, 1)), mode='constant')
        x_result = np.zeros_like(image)
        y_result = np.zeros_like(image)

        rows, cols = image.shape
        for i in range(1,rows):
            for j in range(1,cols):
                region = padded[i:i + 3, j:j + 3]
                x_result[i, j] = np.sum(region * self.sobel_x)
                y_result[i, j] = np.sum(region * self.sobel_y)

        gradient = np.sqrt(x_result ** 2 + y_result ** 2)
        threshold = gradient.mean()
        gradient = np.where(gradient >= threshold, 255, 0)
        gradient = gradient.astype(np.uint8)

        return np.clip(gradient, 0, 255)

    def apply_on_grayscale(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the edge detection operation on a grayscale image.
        :param image: The grayscale image as a NumPy array.
        :return: The modified image.
        """
        return self.padded_conv(image).astype(np.uint8)
