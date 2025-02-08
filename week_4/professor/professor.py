from random import randint
import sys


def get_level():
    while True:
        try:
            result = int(input("Level: "))
            assert 1 <= result <= 3
            break
        except EOFError:
            sys.exit(1)
        except:
            continue

    return result


def generate_integer(level):
    # Level 1 : 0 -> 9
    # Level 2 : 10 -> 99
    # Level 3 : 100 -> 999
    min_nb = pow(10, level - 1)

    # EDGE CASE : 0 is a one-digit non negative number
    if min_nb == 1:
        min_nb = 0

    max_nb = pow(10, level) - 1

    return randint(min_nb, max_nb)


def main():
    score = 0

    level = get_level()

    for tries in range(10):
        nb1 = generate_integer(level)
        nb2 = generate_integer(level)

        expected_result = nb1 + nb2

        # Set current_result to -1 in case user fails on 0 + 0
        current_result = -1

        for cur_try in range(3):
            try:
                current_result = int(input(f"{nb1} + {nb2} = "))
                assert current_result == expected_result
                if expected_result == current_result:
                    score += 1
                    break
            except EOFError:
                sys.exit(1)
            except:
                print("EEE")

        if current_result != expected_result:
            print(f"{nb1} + {nb2} = {expected_result}")

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
