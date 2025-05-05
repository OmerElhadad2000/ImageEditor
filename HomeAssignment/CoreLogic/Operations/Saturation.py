import numpy as np

from CoreLogic.Operations.BaseOperation import BaseOperation
from Infrastructure.Utils import Utils


class Saturation(BaseOperation):
    def __init__(self):
        """
        Initialize the Saturation operation.
        """
        self.filter_amount = 1

    def set_filter_amount(self, filter_amount: float):
        """
        Set the saturation adjustment value.
        :param filter_amount: The saturation adjustment value.
        """
        self.filter_amount = filter_amount

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Apply the saturation adjustment to the image.
        The image is converted to float64 to avoid overflow and underflow issues.
        The image is then clipped to the range [0, 255] and converted back to uint8.
        :param image: The image as a NumPy array.
        :return: The modified image.
        """
        image = image.astype(np.float64)
        hsv_image = Utils.rgb_to_hsv(image)
        hsv_image[..., 1] *= self.filter_amount
        hsv_image[..., 1] = np.clip(hsv_image[..., 1], 0, 1)  # Because HSV is in [0, 1] range

        rgb_image = Utils.hsv_to_rgb(hsv_image)
        rgb_image = np.clip(rgb_image, 0, 255)
        rgb_image = rgb_image.astype(np.uint8)
        return rgb_image
