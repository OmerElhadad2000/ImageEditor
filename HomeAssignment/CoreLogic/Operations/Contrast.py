import numpy as np

from CoreLogic.Operations.BaseOperation import BaseOperation


class Contrast(BaseOperation):

    def __init__(self):
        """
        Initialize the Contrast operation.
        """
        self.filter_amount = 0.5

    def configure(self, **kwargs) -> None:
        self.filter_amount = kwargs.get("value", 0.5)

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the contrast adjustment to the image, by multiplying each pixel by a scalar value.
        We convert the image to float64 to avoid overflow and underflow issues.
        The image is then clipped to the range [0, 255] and converted back to uint8.
        :param image: The image as a NumPy array.
        :return: The modified image.
        """
        image = image.astype(np.float64)
        image = self.filter_amount * (image - 128) + 128  # 128 is the midpoint of 0-255 range and will be grayish if 0
        image = np.clip(image, 0, 255)
        image = image.astype(np.uint8)
        return image
