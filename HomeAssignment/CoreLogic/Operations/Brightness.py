import numpy as np
from CoreLogic.Operations.BaseOperation import BaseOperation


class Brightness(BaseOperation):
    def __init__(self):
        """
        Initialize the Brightness operation.
        """
        self.filter_amount = 0

    def configure(self, **kwargs) -> None:
        self.filter_amount = kwargs.get("value", 0)

    def apply(self, image: np.ndarray) -> np.ndarray:
        result = image.astype(np.float64)
        result += self.filter_amount
        result = np.clip(result, 0, 255)
        image = result.astype(np.uint8)
        return image
