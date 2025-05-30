import json


class Parser:

    def __init__(self, file_path: str):
        self.file = open(file_path)
        self.json_data = json.load(self.file)

    def validate_json(self) -> None:
        """
        Validate the JSON data file, ensuring the given instructions of the project
        are met for the file, and is structured as described.
        :return: True if meets the requirements, False otherwise.
        """
        if self.json_data is None:
            raise ValueError("JSON data is None. Please check the file path.")

        if not self.is_valid_path(self.json_data['input']):
            raise ValueError("Input key not found in JSON data or path is invalid. Please check the file path.")

        if not self.json_data["output"] and not self.json_data["display"]:
            raise ValueError("Output key or display command are missing. Please fill at least one.")

    def get_operations(self) -> list:
        """
        Get the operations from the JSON data.
        :return: A list of operations.
        """
        return self.json_data["operations"]

    def get_image_path(self) -> str:
        """
        Get the image path from the JSON data.
        :return: The image path.
        """
        return self.json_data["input"]

    def get_output_path(self) -> str:
        """
        Get the output path from the JSON data.
        :return: The output path.
        """
        return self.json_data["output"]

    def get_display(self) -> bool:
        """
        Get the display command from the JSON data.
        :return: The display command.
        """
        return self.json_data["display"]

    @staticmethod
    def is_valid_path(path: str) -> bool:
        """
        Check if the path is valid.
        :param path: The path to check.
        :return: True if valid, False otherwise.
        """
        try:
            with open(path, 'r') as f:
                return True
        except FileNotFoundError:
            return False
