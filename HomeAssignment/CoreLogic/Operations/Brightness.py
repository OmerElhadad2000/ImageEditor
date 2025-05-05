import numpy as np
from CoreLogic.Operations.BaseOperation import BaseOperation


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
        result = image[:, :, :3].astype(np.float64)
        result += self.filter_amount
        result = np.clip(result, 0, 255)
        image[:, :, :3] = result.astype(np.uint8)
        return image

