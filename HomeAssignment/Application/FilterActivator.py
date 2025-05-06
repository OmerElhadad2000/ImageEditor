import numpy as np
from CoreLogic.Operations.BoxBlur import BoxBlur
from CoreLogic.Operations.Brightness import Brightness
from CoreLogic.Operations.Contrast import Contrast
from CoreLogic.Operations.EdgeDetection import EdgeDetection
from CoreLogic.Operations.Saturation import Saturation
from CoreLogic.Operations.Sharpen import Sharpen


class FilterActivator:

    def __init__(self):
        self.filters = {
            "brightness": Brightness(),
            "saturation": Saturation(),
            "contrast": Contrast(),
            "box": BoxBlur(),
            "sobel": EdgeDetection(),
            "sharpen": Sharpen(),
        }

    def activate_filter(self, filter_data: dict, image: np.ndarray) -> np.ndarray:
        filter_type = filter_data["type"]
        operation = self.filters[filter_type]
        operation.configure(**filter_data)
        return operation.apply(image)
