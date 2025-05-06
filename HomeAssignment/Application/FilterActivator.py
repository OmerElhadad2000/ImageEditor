import numpy as np
from CoreLogic.Operations.BoxBlur import BoxBlur
from CoreLogic.Operations.Brightness import Brightness
from CoreLogic.Operations.Contrast import Contrast
from CoreLogic.Operations.EdgeDetection import EdgeDetection
from CoreLogic.Operations.Saturation import Saturation
from CoreLogic.Operations.Sharpen import Sharpen


class FilterActivator:

    def __init__(self):
        """
        Initialize the FilterActivator.
        """
        self.brightness = Brightness()
        self.saturation = Saturation()
        self.contrast = Contrast()
        self.box_blur = BoxBlur()
        self.edge_detection = EdgeDetection()
        self.sharpen = Sharpen()

    def activate_filter(self, filter_data: dict, image: np.ndarray) -> np.ndarray:
        if filter_data["type"] == "brightness":
            self.brightness.set_filter_amount(filter_data["value"])
            return self.brightness.apply(image)
        elif filter_data["type"] == "saturation":
            self.saturation.set_filter_amount(filter_data["value"])
            return self.saturation.apply(image)
        elif filter_data["type"] == "contrast":
            self.contrast.set_filter_amount(filter_data["value"])
            return self.contrast.apply(image)
        elif filter_data["type"] == "box":
            self.box_blur.set_blur_window(filter_data["height"], filter_data["width"])
            return self.box_blur.apply(image)
        elif filter_data["type"] == "sobel":
            return self.edge_detection.apply(image)
        elif filter_data["type"] == "sharpen":
            self.sharpen.set_filter_amount(filter_data["value"])
            return self.sharpen.apply(image)
        else:
            raise ValueError(f"Unknown filter type: {filter_data['type']}")
