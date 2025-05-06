from PIL import Image
import numpy as np

from Infrastructure.Utils import Utils


class ImageIO:
    @staticmethod
    def read_image(image_path: str) -> np.ndarray:
        """
        Read an image from a file.

        :param image_path: The path to the image file.
        :return: The image as a NumPy array.
        """

        with Image.open(image_path) as img:
            img = np.array(img)
            return Utils.convert_to_3d(img)

    @staticmethod
    def write_image(image: np.ndarray, output_path: str) -> None:
        """
        Write an image to a file.

        :param image: The image as a NumPy array.
        :param output_path: The path where the image will be saved.
        """
        img = Image.fromarray(image)
        img.save(output_path)

    @staticmethod
    def show_image(image: np.ndarray) -> None:
        """
        Display an image.

        :param image: The image as a NumPy array.
        """
        img = Image.fromarray(image)
        img.show()
