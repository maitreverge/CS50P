names = []

# Without specifing it, open will open the targeted file in `READ` mode
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"Hello, {name}")

# ! Better implementation


with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}")