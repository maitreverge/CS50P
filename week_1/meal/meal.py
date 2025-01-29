def make_prompt(sentence: str):
    print(f"{sentence}: ", end="")
    return input()


def main():
    """
    7:00 -> 8:00 : breakfast time
    12:00 -> 13:00 : lunch time
    18:00 -> 19:00 : dinner time
    """

    prompt = make_prompt("What time is it?")

    time_float = convert(prompt)

    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")


def convert(time):

    a, b = time.split(":")

    hours = int(a)
    minutes = int(b) / 60

    return hours + minutes


if __name__ == "__main__":
    main()
