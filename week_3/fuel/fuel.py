import sys


def main():

    while True:
        prompt = input("Fraction: ")

        try:
            x, y = prompt.split("/")
            val_1, val_2 = int(x), int(y)

            assert val_1 <= val_2

            result = (val_1 / val_2) * 100

            if result <= 1:
                print(f"E")
            elif result >= 99:
                print(f"F")
            else:
                print(f"{result:.0f}%")

            break
        except (ValueError, ZeroDivisionError, AssertionError):
            continue


if __name__ == "__main__":
    main()
