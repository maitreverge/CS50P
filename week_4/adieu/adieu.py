import inflect


def main():
    p = inflect.engine()

    names = list()
    while True:
        try:
            prompt = input("Name: ").capitalize()
            names.append(prompt)
        except EOFError:
            break

    print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
