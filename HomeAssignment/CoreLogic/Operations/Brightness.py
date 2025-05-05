import numpy as np

from CoreLogic.Operations.base_operation import BaseOperation


class Brightness(BaseOperation):
    def __init__(self):
        """
        Initialize the Brightness operation.
        """
        self.filter_amount = 0

    def set_filter_amount(self, filter_amount: float):
        """
        Set the brightness adjustment value.
        :param filter_amount: The brightness adjustment value.
        """
        self.filter_amount = filter_amount

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the brightness adjustment to the image, by adding a scalar value to each pixel.
        We convert the image to float64 to avoid overflow and underflow issues.
        The image is then clipped to the range [0, 255] and converted back to undefined int fitting pixel def.
        :param image: The image as a NumPy array.
        :return: The modified image.
        """
        image = image.astype(np.float64)
        image += self.filter_amount
        image = np.clip(image, 0, 255)
        image = image.astype(np.uint8)
        return image
