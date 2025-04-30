import sys
import os
from PIL import Image, ImageOps


def print_usage(message):
    print(message)
    print("Usage : python3 shirt.py img1.png img2.jpeg")
    sys.exit(1)


def parse_args(args):
    if len(sys.argv) != 3:
        print_usage("Incorrect number of arguments")

    valid_extension = ("jpeg", "jpg", "png")

    input_file = str(args[1])
    output_file = str(args[2])

    # Extract what's after the last found dot.
    # Lower the results for checking case insensitively
    ext_input = input_file[input_file.rfind(".") + 1 :].lower()
    ext_output = output_file[output_file.rfind(".") + 1 :].lower()

    correct_extension = ext_output in valid_extension and ext_input in valid_extension
    similar_extensions = ext_input == ext_output

    if not correct_extension or not similar_extensions:
        print_usage("Arguments must be of the same similar extension")

    # Checks if the file both exists and is readeable
    if not os.access(input_file, os.R_OK):
        print_usage("File not found")

    return input_file, output_file


def main():
    input_file, output_file = parse_args(sys.argv)

    with Image.open("shirt.png") as shirt:
        shirt_size = shirt.size

        with Image.open(input_file) as img:
            # Resize and cropped image
            img = ImageOps.fit(img, shirt_size)
            # Third argument is a mask of the shirt image
            img.paste(shirt, (0, 0), shirt)
            img.save(output_file)


if __name__ == "__main__":
    main()
