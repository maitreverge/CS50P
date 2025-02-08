from random import randrange
import sys


def prompt_positive(display: str) -> int:

    while True:
        try:
            result = int(input(display))
            assert result > 0
            break
        except EOFError:
            sys.exit(0)
        except:
            continue

    return result


def main():

    level = prompt_positive("Level: ")
    random_nb = randrange(1, level)

    while True:
        guess = prompt_positive("Guess: ")

        if guess == random_nb:
            print("Just right!")
            break
        elif guess < random_nb:
            print("Too small!")
        else:
            print("Too large!")


if __name__ == "__main__":
    main()
