from PIL import Image
import numpy as np


class ImageIO:
    """
    A class for reading and writing images.
    """

    @staticmethod
    def read_image(image_path: str) -> np.ndarray:
        """
        Read an image from a file.

        :param image_path: The path to the image file.
        :return: The image as a NumPy array.
        """

        with Image.open(image_path) as img:
            return np.array(img)

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

# img = ImageIO.read_image("gray_image.jpg")
# blur = BoxBlur()
# blur.set_blur_window(3,3)
# ImageIO.write_image(blur.apply_on_grayscale(img), "blurred_image.jpg")


# img = ImageIO.read_image("gray_image.jpg")
# sharpen = Sharpen()
# sharpen.set_filter_amount(1.5)
# ImageIO.write_image(sharpen.apply_on_channel(img), "blurred_image.jpg")
