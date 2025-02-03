import sys


def main():

    grocery = dict()
    while True:
        try:
            prompt = input("").lower().strip(" ")
            if prompt in grocery:
                grocery[prompt] += 1
            else:
                grocery[prompt] = 1
        except EOFError:
            break

    sorted_dict = dict(sorted(grocery.items(), key=lambda items: items[0]))
    for items, numbers in sorted_dict.items():
        print(f"{numbers} {items.upper()}")


if __name__ == "__main__":
    main()
