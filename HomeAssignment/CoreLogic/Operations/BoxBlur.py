import numpy as np

from CoreLogic.Operations.BaseOperation import BaseOperation
from CoreLogic.ImageUtils import ImageUtils


class BoxBlur(BaseOperation):
    def __init__(self):
        self.X = 1
        self.Y = 1

    def configure(self, **kwargs) -> None:
        self.X = kwargs.get("height", 1)
        self.Y = kwargs.get("width", 1)

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the box blur filter to the image.
        The image is expected to be in RGB format (3 channels).
        The box blur is applied to each channel separately, and then merged back together.
        :param image: The image as a NumPy array.
        :return: The modified image with box blur applied.
        """
        return ImageUtils.multi_channel_filter_apply(image, self.blur_channel)

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

