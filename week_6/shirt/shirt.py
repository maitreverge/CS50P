import sys
import csv
import os


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
    ext_input = input_file[input_file.rfind(".") + 1:].lower()
    ext_output = output_file[output_file.rfind(".") + 1:].lower()

    correct_extension = (ext_output in valid_extension and ext_input in valid_extension)
    similar_extensions = ext_input == ext_output


    if not correct_extension or not similar_extensions:
        print_usage("Incorrect file extension")

    # print(ext_input)



    # Checks if the file both exists and is readeable
    if not os.access(input_file, os.R_OK):
        print_usage("File not found")

    return input_file, output_file


def main():
    parse_args(sys.argv)



if __name__ == "__main__":
    main()
