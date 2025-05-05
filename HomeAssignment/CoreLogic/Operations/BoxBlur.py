import numpy as np

from CoreLogic.Operations.BaseOperation import BaseOperation


class BoxBlur(BaseOperation):
    """
    BoxBlur operation class that applies a box blur filter to an image.
    """

    def __init__(self):
        """
        Initialize the BoxBlur operation.
        """
        self.X = 1
        self.Y = 1

    def set_blur_window(self, X: int, Y: int):
        """
        Set the box blur amount.
        """
        if X > 0 and Y > 0:
            self.X, self.Y = X, Y

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the box blur filter to the image.
        The image is expected to be in RGB format (3 channels).
        The box blur is applied to each channel separately, and then merged back together.
        :param image: The image as a NumPy array.
        :return: The modified image with box blur applied.
        """
        red_channel = image[:, :, 0]
        green_channel = image[:, :, 1]
        blue_channel = image[:, :, 2]

        red_result = self.blur_channel(red_channel)
        green_result = self.blur_channel(green_channel)
        blue_result = self.blur_channel(blue_channel)
        result = np.zeros_like(image)

        result[:, :, 0] = red_result
        result[:, :, 1] = green_result
        result[:, :, 2] = blue_result
        return result.astype(np.uint8)

    def blur_channel(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the box blur operator to the image using a padded convolution.
        The image is padded to handle the borders.
        :param image: The image as a NumPy array.
        :return: The modified image with box blur applied.
        """
        image = image.astype(np.float32)
        pad_x = self.X // 2
        pad_y = self.Y // 2
        padded = np.pad(image, ((pad_x, pad_x), (pad_y, pad_y)), mode='constant', constant_values=0)
        result = np.zeros_like(image)

        rows, cols = image.shape
        for i in range(rows):
            for j in range(cols):
                region = padded[i:i + self.X, j:j + self.Y]
                result[i, j] = np.mean(region)
        result = np.clip(result, 0, 255)
        result = result.astype(np.uint8)
        return result

