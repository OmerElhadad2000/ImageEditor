import argparse

from Application.FilterActivator import FilterActivator
from Infrastructure.ImageIO import ImageIO
from Application.Parser import Parser


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Edit an image based on a JSON configuration file.")
    parser.add_argument('--config', type=str, required=True, help="Path to the JSON configuration file.")

    # Parse arguments
    args = parser.parse_args()
    json_file_path = args.config

    # Load and validate the JSON file
    try:
        parser = Parser(json_file_path)
        parser.validate_json()
    except Exception as e:
        raise ValueError(f"Error validating JSON file: {e}")

    # Get operations from the JSON file
    operations = parser.get_operations()

    # Get image path
    image_path = parser.get_image_path()
    image = ImageIO.read_image(image_path)
    filter_activator = FilterActivator()
    for operation in operations:
        image = filter_activator.activate_filter(operation, image)

    # Get output path
    output_path = parser.get_output_path()
    if output_path:
        ImageIO.write_image(image, output_path)
    else:
        ImageIO.show_image(image)


if __name__ == '__main__':
    main()
