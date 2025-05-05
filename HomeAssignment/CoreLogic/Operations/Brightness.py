import numpy as np

from CoreLogic.Operations.base_operation import BaseOperation
from Infrastructure.Utils import Utils


class Brightness(BaseOperation):
    def __init__(self):
        """
        Initialize the Brightness operation.
        :param filter_amount: The brightness adjustment value.
        """
        self.filter_amount = 0
    def set_filter_amount(self, filter_amount: float):
        """
        Set the brightness adjustment value.
        :param filter_amount: The brightness adjustment value.
        """
        self.filter_amount = filter_amount
    def apply(self, image: np.ndarray) -> np.ndarray:
        image = image.astype(np.float64)
        image += self.filter_amount
        image = np.clip(image, 0, 255)
        image = image.astype(np.uint8)
        return image
