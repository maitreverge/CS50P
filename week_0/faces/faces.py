def convert():
    user_input = input()
    user_input = user_input.replace(":)", "🙂")
    user_input = user_input.replace(":(", "🙁")
    print(user_input)


if __name__ == "__main__":
    convert()
