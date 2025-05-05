from abc import ABC, abstractmethod
import numpy as np


class BaseOperation(ABC):
    """
    Abstract base class for operations.
    """

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the operation to the image.
        :param image: The image to which the operation will be applied.
        :return: The modified image.
        """
