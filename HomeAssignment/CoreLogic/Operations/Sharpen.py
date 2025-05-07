import numpy as np

from CoreLogic.Operations.BaseOperation import BaseOperation
from CoreLogic.Operations.BoxBlur import BoxBlur
from CoreLogic.ImageUtils import ImageUtils


class Sharpen(BaseOperation):
    def __init__(self):
        self.filter_amount = 1

    def configure(self, **kwargs) -> None:
        self.filter_amount = kwargs.get("value", 1)

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the sharpening filter to the image.
        The image is expected to be in RGB format (3 channels).
        The sharpening is applied to each channel separately, and then merged back together.
        :param image: The image as a NumPy array.
        :return: The modified image with sharpening applied.
        """
        return ImageUtils.multi_channel_filter_apply(image, self.sharpen_channel)

    def sharpen_channel(self,image: np.ndarray) -> np.ndarray:
        """
        Apply the sharpening operator to the image using a padded convolution.
        The image is padded to handle the borders.
        The sharpening is done by subtracting a blurred version of the image from the original image.
        :param image: The image as a NumPy array.
        :return: The modified image with sharpening applied.
        """
        blur = BoxBlur()
        blur.configure(height=5, width=5)
        blurred = blur.blur_channel(image).astype(np.float32)

        image = image.astype(np.float32)
        sharpened = image + self.filter_amount * (image - blurred)
        return np.clip(sharpened, 0, 255).astype(np.float32)


