from abc import ABC, abstractmethod
import np


class BaseOperation(ABC):
    """
    Abstract base class for operations.
    """

    def apply(self, filter_amount: float, image: np.ndarray) -> np.ndarray:
        """
        Apply the operation to the image.

        :param filter_amount: The amount change to be applied.
        :param image: The image to which the operation will be applied.
        :return: The modified image.
        """
        pass
