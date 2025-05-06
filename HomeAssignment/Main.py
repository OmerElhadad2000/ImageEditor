import argparse

from Application.FilterActivator import FilterActivator
from Infrastructure.ImageIO import ImageIO
from Application.Parser import Parser


def main():
    """
    Main function to run the image editing application.
    This function parses command line arguments, validates the JSON configuration file,
    and applies the specified operations to the image.

    NOTE: The arg parser for filepath that is used here, is written with the chat's help.
    When I first began working, I have tried building it on my own, but encountered problems
    regarding the --config so the chat suggested trying this.
    """
    parser = argparse.ArgumentParser(description="Edit an image based on a JSON configuration file.")
    parser.add_argument('--config', type=str, required=True, help="Path to the JSON configuration file.")

    args = parser.parse_args()
    json_file_path = args.config

    try:
        parser = Parser(json_file_path)
        parser.validate_json()
    except Exception as e:
        raise ValueError(f"Error validating JSON file: {e}")

    operations = parser.get_operations()

    image_path = parser.get_image_path()
    image = ImageIO.read_image(image_path)

    filter_activator = FilterActivator()

    for operation in operations:
        image = filter_activator.activate_filter(operation, image)

    output_path = parser.get_output_path()

    if output_path:
        ImageIO.write_image(image, output_path)

    if parser.get_display():
        ImageIO.show_image(image)


if __name__ == '__main__':
    main()
