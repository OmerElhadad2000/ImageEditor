import numpy as np

from CoreLogic.Operations.BaseOperation import BaseOperation
from CoreLogic.Operations.BoxBlur import BoxBlur


class Sharpen(BaseOperation):
    """
    A class to apply a sharpening filter to an image.
    """

    def __init__(self):
        """
        Initialize the Sharpen operation.
        """
        self.filter_amount = 3

    def set_filter_amount(self, filter_amount: float):
        """
        Set the sharpening amount.
        :param filter_amount: The sharpening amount.
        """
        if filter_amount >= 0:
            self.filter_amount = filter_amount

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the sharpening filter to the image.
        The image is expected to be in RGB format (3 channels).
        The sharpening is applied to each channel separately, and then merged back together.
        :param image: The image as a NumPy array.
        :return: The modified image with sharpening applied.
        """
        red_channel = image[:, :, 0]
        green_channel = image[:, :, 1]
        blue_channel = image[:, :, 2]

        red_result = self.sharpen_channel(red_channel)
        green_result = self.sharpen_channel(green_channel)
        blue_result = self.sharpen_channel(blue_channel)
        result = np.zeros_like(image)

        result[:, :, 0] = red_result
        result[:, :, 1] = green_result
        result[:, :, 2] = blue_result
        return result.astype(np.uint8)

    def sharpen_channel(self, image: np.ndarray) -> np.ndarray:
        blur = BoxBlur()
        blur.set_blur_window(5, 5)
        blurred = blur.blur_channel(image).astype(np.float32)

        image = image.astype(np.float32)
        sharpened = image + self.filter_amount * (image - blurred)
        return np.clip(sharpened, 0, 255).astype(np.uint32)


