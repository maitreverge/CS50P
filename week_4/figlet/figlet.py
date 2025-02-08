import sys
from pyfiglet import Figlet
import random


def clean_exit():
    print("Invalid usage")
    sys.exit(1)


# NO ARGV or <-f> // <--font>  + font
def parse_argv(argv, figlet) -> str:
    fonts = figlet.getFonts()  # List
    len_argv = len(sys.argv)

    if len_argv == 1:  # no ARGV provided => random font
        return random.choice(fonts)
    elif len_argv == 3:
        f = ["-f", "--font"]
        if sys.argv[1] not in f or sys.argv[2] not in fonts:
            clean_exit()
        return sys.argv[2]
    else:
        clean_exit()


def main():

    figlet = Figlet()
    use_font = parse_argv(sys.argv, figlet)

    prompt = input("Input: ")
    figlet.setFont(font=use_font)
    print(figlet.renderText(prompt))


if __name__ == "__main__":
    main()
