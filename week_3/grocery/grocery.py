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


    for items, numbers in grocery.items()
        print(f"{numbers} {items.capitalize()}")





if __name__ == "__main__":
    main()
