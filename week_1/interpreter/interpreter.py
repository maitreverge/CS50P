def make_prompt(sentence: str):
    print(f"{sentence}: ", end="")
    return input()


def main():
    prompt = make_prompt("Expression")

    x, operator, y = prompt.split(" ")

    nb1 = int(x)
    nb2 = int(y)

    result = int()

    match operator:
        case "+":
            result = nb1 + nb2
        case "-":
            result = nb1 - nb2
        case "*":
            result = nb1 * nb2
        case "/":
            result = nb1 / nb2

    print(f"{result:.1f}")


if __name__ == "__main__":
    main()
