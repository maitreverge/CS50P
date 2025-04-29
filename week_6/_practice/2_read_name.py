# Initial implementation
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(f"Hello, {line}", end="")

# Better implementation

with open("names.txt", "r") as file:
    # With the open method, we can justb simply loop over the fd,
    # and that just gives us every line everytime we loop over it
    for line in file:
        print("Hello,", line.rstrip())