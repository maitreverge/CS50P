def main():
    prompt = input("Fraction: ")
    fraction = convert(prompt)
    print(f"{gauge(fraction)}")


def convert(fraction):
    x, y = fraction.split("/")
    val_1, val_2 = int(x), int(y)

    if val_2 == 0:
        raise ZeroDivisionError

    if val_1 > val_2:
        raise ValueError

    return (val_1 / val_2) * 100


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
